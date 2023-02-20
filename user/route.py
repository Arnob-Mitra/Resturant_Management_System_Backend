from error.exception import EntityNotFoundError, Unauthorized
from user.dto import ResponseDTO, CreateDTO, UpdateUserDTO, LoginDTO
from user.model import User
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from uuid import UUID
from pymongo import ReturnDocument
import bcrypt

router = APIRouter()

@router.post('/login')
async def create(data:LoginDTO):
    try:
        print(data)
        user = await User.find_one(User.phone == data.phone)
        if user is not None and bcrypt.checkpw(data.password, user.password):
            return{'success':True, 'message': 'User successfully login'}
        else:
            raise Unauthorized
    except Unauthorized as ue:
        return JSONResponse(content={'success': False, 'message': ue.message}, status_code=ue.status_code)
    except Exception as e:
        return JSONResponse(content={'success':False, 'message': str(e)}, status_code=500)

@router.post('/')
async def create(data:CreateDTO):
    try: 
        user = User(**data.dict())
        user.password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
        await user.save()
        return{'success':True, 'message':'User successfully created', 'data':user}
    except Exception as e:
        return JSONResponse(content={'success':False, 'message': str(e)}, status_code=500)

@router.get('/{userId}')
async def get_by_id(userId:UUID):
    try:
        user = await User.get(userId)
        if user is None:
            raise EntityNotFoundError
        return {'success':True, 'message':'Successfully get the user', 'data':ResponseDTO(**user.dict()).dict()}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success':False, 'message': enfe.message}, status_code=enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success':False,'message': str(e)}, status_code=500)
    
@router.get('/')
async def get_all():
    try:
        user = await User.find().to_list()
        if user is None:
            raise EntityNotFoundError
        return {"success":True, "message":"List of all users", 'data':user}
    except Exception as e:
        return JSONResponse(content={'success':False, 'message':(str(e))}, status_code=500)

@router.patch('/{userId}')
async def update(userId:UUID, data:UpdateUserDTO):
    try:
        user = await User.get_motor_collection().find_one_and_update({ '_id': userId}, {'$set': data.dict()}, return_document=ReturnDocument.AFTER)
        # await User.find_one(User.id == userId).update({'$set': data.dict()})
        if user is None:
            raise EntityNotFoundError
        return {'success':True, 'message':'User updated successfully', 'data':user}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success':False, 'message': enfe.message}, status_code=enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success':False,'message': str(e)}, status_code=500)
    

@router.delete('/{userId}')
async def delete(userId:UUID):
    try: 
        user = await User.get_motor_collection().find_one_and_delete({ '_id': userId})
        if user is None:
            raise EntityNotFoundError
        return {'success':True, 'message':'User delate successfully'}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success': False, 'message': enfe.message}, status_code = enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success': False,'message': str(e)}, status_code = 500)
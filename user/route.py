from error.exception import EntityNotFoundError
from user.dto import UserCreateDTO, UpdateUserDTO
from user.model import User
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from uuid import UUID
from pymongo import ReturnDocument

router = APIRouter()

@router.get('/{userId}')
async def get_by_id(userId:UUID):
    try:
        data = await User.get(userId)
        if data is None:
            raise EntityNotFoundError
        return {'success':True, 'message':'Successfully get the user', 'data':data}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success':False, 'message': enfe.message}, status_code=enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success':False,'message': str(e)}, status_code=500)
    
@router.get('/')
async def get_all():
    try:
        data = await User.find().to_list()
        if data is None:
            raise EntityNotFoundError
        return {"success":True, "message":"List of all users", 'data':data}
    except Exception as e:
        return JSONResponse(content={'success':False, 'message':(str(e))}, status_code=500)

@router.post('/')
async def create(data:UserCreateDTO):
    try: 
        data = User(**data.dict())
        await data.save()
        if data is None:
            raise EntityNotFoundError
        return{'success':True, 'message':'User successfully created', 'data':data}
    except Exception as e:
        return JSONResponse(content={'success':False, 'message': str(e)}, status_code=500)


@router.patch('/{userId}')
async def update(userId:UUID, data:UpdateUserDTO):
    try:
        data = await User.get_motor_collection().find_one_and_update({ '_id': userId}, {'$set': data.dict()}, return_document=ReturnDocument.AFTER)
        # await User.find_one(User.id == userId).update({'$set': data.dict()})
        if data is None:
            raise EntityNotFoundError
        return {'success':True, 'message':'User updated successfully', 'data':data}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success':False, 'message': enfe.message}, status_code=enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success':False,'message': str(e)}, status_code=500)
    

@router.delete('/{userId}')
async def delete(userId:UUID):
    try: 
        data = await User.get_motor_collection().find_one_and_delete({ '_id': userId})
        print (data)
        if data is None:
            raise EntityNotFoundError
        return {'success':True, 'message':'User delate successfully'}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success': False, 'message': enfe.message}, status_code = enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success': False,'message': str(e)}, status_code = 500)
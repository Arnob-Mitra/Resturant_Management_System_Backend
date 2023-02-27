from error.exception import EntityNotFoundError, Unauthorized
from user.dto import OwnerCreateDTO, UserCreateDTO, UpdateUserDTO, ResponseDTO, LoginDTO, ChangePasswordDTO
from user.model import User, UserTypeEnum
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from uuid import UUID
from pymongo import ReturnDocument
import bcrypt

router = APIRouter()

@router.post('/login') 
async def create(data:LoginDTO):
    try:
        user = await User.find_one(User.phone == data.phone)
        #if user is not None and bcrypt.checkpw(data.password.encode('utf-8'), user.password.encode('utf-8')):
        return {'success':True, 'message': 'Login successfully'}
#       else:
#            raise Unauthorized
    except Unauthorized as ue:
        return JSONResponse(content={'success': False, 'message': ue.message}, status_code=ue.status_code)
    except Exception as e:
        return JSONResponse(content={'success':False, 'message': str(e)}, status_code=500)
    

@router.post('/')  
async def create(data: OwnerCreateDTO):
    try:
        user = User(**data.dict())
        user.password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
        await user.save()
        if user.user_type is UserTypeEnum.ADMIN:
            return {'success': True, 'message': 'Admin successfully created', 'data':user}
        if user.user_type is UserTypeEnum.RESTAURANT:
            return {'success': True, 'message': 'Restaurant successfully created', 'data': user}
    except Exception as e:
        return JSONResponse(content={'success':False, 'message': str(e)}, status_code = 500)
 
 
@router.post('/userCreation') 
async def createUser(data: UserCreateDTO):
    try: 
        user = User(**data.dict())
        await user.save()
        return {'success': True, 'message': 'User created successfully', 'data': user}
    except Exception as e :
        return JSONResponse(content={'success': False, 'message': str(e)}, status_code = 500)
    

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
        return JSONResponse(content={'success':False,'message': str(e)}, status_code = 500) 
    
    
@router.get('/')
async def get_all():
    try:
        user = await User.find().to_list()
        if user is None:
            raise EntityNotFoundError
        return {"success":True, "message":"List of all types of users", 'data':user}
    except Exception as e:
        return JSONResponse(content={'success':False, 'message':(str(e))}, status_code = 500)
    

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
 
 
@router.patch('/cha/{user_Id}')
async def changePassword(user_Id:UUID, data:ChangePasswordDTO):
    try:
        #user = await User.find_one(User.password == data.old_password).update({'$set': data.dict()})
        user = await User.get_motor_collection().find_one_and_update({ '_id': user_Id}, {'$set': data.dict()}, return_document=ReturnDocument.AFTER)
        return {'success':True, 'message':'Password has been changed successfully'}
    except Exception as e:
        return JSONResponse(content={'success':False, 'message': str(e)}, status_code = 500)
    
    
@router.delete('/{userId}')
async def delete(userId:UUID):
    try: 
        user = await User.get_motor_collection().find_one_and_delete({ '_id': userId})
        if user is None:
            raise EntityNotFoundError
        return {'success':True, 'message':'Delete successfully'}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success': False, 'message': enfe.message}, status_code = enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success': False,'message': str(e)}, status_code = 500)
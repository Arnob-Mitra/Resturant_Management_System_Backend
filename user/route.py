from error.exception import EntityNotFoundError, Unauthorized
from middleware.hash import ACCESS_TOKEN_EXPIRE_MINUTES, REFRESH_TOKEN_EXPIRE_MINUTES, create_access_token, create_refresh_token
from user.dto import OwnerCreateDTO, UserCreateDTO, UpdateUserDTO, ResponseDTO, LoginDTO, ChangePasswordDTO
from user.model import User, UserTypeEnum
from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from uuid import UUID
from pymongo import ReturnDocument
import bcrypt

router = APIRouter()

#ABCDEF put the status code as shown in here for all requests
#ABCDEF get_all function should have query parameters for efficient finding and filtering
#ABCDEF get_all function should have two extra parameters skip and limit for pagination purposes
#ABCDEF all patch function should also update the "updated_at" field

@router.post('/login', status_code=200) 
async def create(data:LoginDTO):
    try:
        user = await User.find_one(User.phone == data.phone)
        if user is not None and bcrypt.checkpw(data.password.encode('utf-8'), user.password.encode('utf-8')):
            access_token = create_access_token(user.id, ACCESS_TOKEN_EXPIRE_MINUTES)
            refresh_token = create_refresh_token(user.id, REFRESH_TOKEN_EXPIRE_MINUTES)
            return {'success': True, 'message': 'Login successfully', 'data': {'access_token': access_token, 'refresh_token': refresh_token}}
        else:
            raise Unauthorized
    except Unauthorized as ue:
        return JSONResponse(content={'success': False, 'message': ue.message}, status_code=ue.status_code)
    except Exception as e:
        return JSONResponse(content={'success': False, 'message': str(e)}, status_code=500)
    

@router.post('')  
async def create(data: OwnerCreateDTO):
    try:
        user = User(**data.dict())
        user.password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
        await user.save()
        access_token = create_access_token(user.id, ACCESS_TOKEN_EXPIRE_MINUTES)
        refresh_token = create_refresh_token(user.id, REFRESH_TOKEN_EXPIRE_MINUTES)
        if user.user_type is UserTypeEnum.ADMIN:
            return {'success': True, 'message': 'Admin successfully created', 'data': {'user': user, 'access-token': access_token, 'refresh-token': refresh_token}}
        if user.user_type is UserTypeEnum.RESTAURANT:
            return {'success': True, 'message': 'Restaurant successfully created', 'data': {'user': user, 'access-token': access_token, 'refresh-token': refresh_token}}
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
    

@router.get('/{userId}', status_code=200)
async def get_by_id(userId:UUID):
    try:
        user = await User.get(userId)
        if user is None:
            raise EntityNotFoundError
        return {'success': True, 'message': 'Successfully get the user', 'data': ResponseDTO(**user.dict()).dict()}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success': False, 'message': enfe.message}, status_code=enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success': False,'message': str(e)}, status_code=500) 
    
    
@router.get('', status_code = 200)
async def get(phone: str = None, name: str = None, email:str = None):
    try:
        criteria = {}
        if phone is not None:
            criteria['phone'] = phone
        if name is not None:
            criteria['name'] = name
        if email is not None:
            criteria['email'] = email
        user = await User.find(criteria).to_list()
        return {'success': True, 'message':'List of all types of users', 'data': user}
    except Exception as e:
        return JSONResponse(content={'success':False, 'message':(str(e))}, status_code = 500)
    

@router.patch('/{userId}', status_code=200)
async def update(userId:UUID, data:UpdateUserDTO):
    try:
        user = await User.get_motor_collection().find_one_and_update({ '_id': userId}, {'$set': data.dict()}, return_document=ReturnDocument.AFTER)
        if user is None:
            raise EntityNotFoundError
        return {'success': True, 'message': 'User updated successfully', 'data': user}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success': False, 'message': enfe.message}, status_code=enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success': False,'message': str(e)}, status_code=500)  
 
 
@router.patch('/cha/{user_Id}', status_code=200)
async def changePassword(user_Id:UUID, data:ChangePasswordDTO):
    try:
        user = await User.get_motor_collection().find_one_and_update({ '_id': user_Id}, {'$set': data.dict()}, return_document=ReturnDocument.AFTER)
        return {'success': True, 'message': 'Password has been changed successfully', 'data': user}
    except Exception as e:
        return JSONResponse(content={'success':False, 'message': str(e)}, status_code=500)
    
    
@router.delete('/{userId}', status_code=200)
async def delete(userId:UUID):
    try: 
        user = await User.get_motor_collection().find_one_and_delete({ '_id': userId})
        if user is None:
            raise EntityNotFoundError
        return {'success': True, 'message': 'Delete successfully'}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success': False, 'message': enfe.message}, status_code=enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success': False,'message': str(e)}, status_code=500)
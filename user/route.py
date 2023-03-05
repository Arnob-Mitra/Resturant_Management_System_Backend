from error.exception import EntityNotFoundError, Unauthorized
from middleware.hash import ACCESS_TOKEN_EXPIRE_MINUTES, REFRESH_TOKEN_EXPIRE_MINUTES, create_access_token, create_refresh_token
from user.dto import CreateDTO, UpdateDTO, ResponseDTO, LoginDTO, ChangePasswordDTO
from user.model import User, UserTypeEnum
from utils import utils


from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pymongo import ReturnDocument
from uuid import UUID
import bcrypt
from datetime import datetime

router = APIRouter()

 
@router.post('/login', status_code=200)
async def login(data: LoginDTO):
    try:
        user = await User.find_one(User.phone == data.phone)
        
        if user is not None and bcrypt.checkpw(data.password.encode('utf-16'), user.password.encode('utf-16')):
            access_token = create_access_token(user.id, ACCESS_TOKEN_EXPIRE_MINUTES) 
            refresh_token = create_refresh_token(user.id, REFRESH_TOKEN_EXPIRE_MINUTES)
            
            user.last_login = datetime.now()
            await user.save()
            
            return {'success': True, 'message': 'Login successfully', 'data': {'access_token': access_token, 'refresh_token': refresh_token}}
        else:
            raise Unauthorized
    except Unauthorized as ue:
        return JSONResponse(content={'success': False, 'message': ue.message}, status_code=ue.status_code)
    except Exception as e:
        return JSONResponse(content={'success': False, 'message': str(e)}, status_code=500)
    

@router.post('')
async def create(data: CreateDTO):
    try:
        user = User(**data.dict())  
        user.password = bcrypt.hashpw(user.password.encode('utf-16'), bcrypt.gensalt())
        
        await user.save()
        
        access_token = create_access_token(user.id, ACCESS_TOKEN_EXPIRE_MINUTES)
        refresh_token = create_refresh_token(user.id, REFRESH_TOKEN_EXPIRE_MINUTES) 
        
        if user.user_type is UserTypeEnum.ADMIN:
            return {'success': True, 'message': 'Admin successfully created', 'data': {'user': user, 'access-token': access_token, 'refresh-token': refresh_token}}
        elif user.user_type is UserTypeEnum.RESTAURANT:
            return {'success': True, 'message': 'Restaurant successfully created', 'data': {'user': user, 'access-token': access_token, 'refresh-token': refresh_token}}
    except Exception as e:
        return JSONResponse(content={'success':False, 'message': str(e)}, status_code = 500)
    
    
@router.get('/{userId}', status_code=200)
async def get_by_id(userId: UUID):
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
async def get(phone: str = None, name: str = None, email:str = None, user_type: UserTypeEnum = None):
    try:
        criteria = {}
        if phone is not None:
            criteria['phone'] = phone
        if name is not None:
            criteria['name'] = name
        if email is not None:
            criteria['email'] = email
        if user_type is not None:
            criteria['user_type'] = user_type
               
        user = await User.find(criteria).to_list()
        return {'success': True, 'message':'List of all types of users', 'data': user}
    except Exception as e:
        return JSONResponse(content={'success':False, 'message':(str(e))}, status_code = 500)
    
    
@router.patch('/{userId}', status_code=200)
async def update(userId: UUID, data: UpdateDTO):
    try:
        doc = utils.create_update_doc(data.dict())
        user = await User.get_motor_collection().find_one_and_update({ '_id': userId}, {'$set': doc}, return_document=ReturnDocument.AFTER)
        
        if user is None:
            raise EntityNotFoundError
        
        return {'success': True, 'message': 'User updated successfully', 'data': user}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success': False, 'message': enfe.message}, status_code=enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success': False,'message': str(e)}, status_code=500)  
 
 
@router.patch('/changePassword/{user_Id}', status_code=200)
async def changePassword(user_Id: UUID, data: ChangePasswordDTO):
    try:
        doc = utils.create_update_doc(data.dict())
        user = await User.get_motor_collection().find_one_and_update({ '_id': user_Id}, {'$set': doc}, return_document=ReturnDocument.AFTER)
         
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
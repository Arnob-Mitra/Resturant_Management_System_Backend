from error.exception import EntityNotFoundError, Unauthorized, NotAcceptable
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

@router.post('/login', status_code=200) #ABCDEF path creation 
async def create(data:LoginDTO):
    try:
        user = await User.find_one(User.phone == data.phone) #ABCDEF check that user phone number(input) and stored phone number (database) are matched or not
        if user is not None and bcrypt.checkpw(data.password.encode('utf-8'), user.password.encode('utf-8')): #ABCDEF check that user password(input) and stored hashed password(database) are matched
            access_token = create_access_token(user.id, ACCESS_TOKEN_EXPIRE_MINUTES)   #ABCDEF then create an access token that is validated for 30mins against that user id 
            refresh_token = create_refresh_token(user.id, REFRESH_TOKEN_EXPIRE_MINUTES) #ABCDEF then create an refresh token that is validated for 30mins against that user id 
            return {'success': True, 'message': 'Login successfully', 'data': {'access_token': access_token, 'refresh_token': refresh_token}} #ABCDEF and return this message
        else:    #ABCDEF otherwise throw the exceptions
            raise Unauthorized
    except Unauthorized as ue:
        return JSONResponse(content={'success': False, 'message': ue.message}, status_code=ue.status_code)
    except Exception as e:
        return JSONResponse(content={'success': False, 'message': str(e)}, status_code=500)
    

@router.post('')  #ABCDEF path creation 
async def create(data: OwnerCreateDTO): #ABCDEF created for admin and restaurant owner
    try:
        user = User(**data.dict())  
        if "+880" not in user.phone:  #ABCDEF check whether the phone number is contained in the bd or not
            raise NotAcceptable
        user.password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()) #ABCDEF hashed that password with salt 
        await user.save()
        access_token = create_access_token(user.id, ACCESS_TOKEN_EXPIRE_MINUTES) #ABCDEF then create an access token that is validated for 30mins against that user id 
        refresh_token = create_refresh_token(user.id, REFRESH_TOKEN_EXPIRE_MINUTES)   #ABCDEF then create an refresh token that is validated for 30mins against that user id 
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
async def get_by_id(userId:UUID):  #ABCDEF get the info by user id 
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
async def get(phone: str = None, name: str = None, email:str = None, user_type: UserTypeEnum = None): #ABCDEF get_all function should have query parameters 
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
async def update(userId:UUID, data:UpdateUserDTO): #ABCDEF created for updating the info of admin and restaurant
    try:
        user = await User.get_motor_collection().find_one_and_update({ '_id': userId}, {'$set': data.dict()}, return_document=ReturnDocument.AFTER) #ABCDEF find that id and set the updated info/data against that id and returned that document  
        if user is None:
            raise EntityNotFoundError
        return {'success': True, 'message': 'User updated successfully', 'data': user}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success': False, 'message': enfe.message}, status_code=enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success': False,'message': str(e)}, status_code=500)  
 
 
@router.patch('/cha/{user_Id}', status_code=200)
async def changePassword(user_Id:UUID, data:ChangePasswordDTO): #ABCDEF created for changing the password
    try:
        user = await User.get_motor_collection().find_one_and_update({ '_id': user_Id}, {'$set': data.dict()}, return_document=ReturnDocument.AFTER) #ABCDEF find that id and set the change the password against that id and returned that document  
        return {'success': True, 'message': 'Password has been changed successfully', 'data': user}
    except Exception as e:
        return JSONResponse(content={'success':False, 'message': str(e)}, status_code=500)
    
    
@router.delete('/{userId}', status_code=200)
async def delete(userId:UUID): 
    try: 
        user = await User.get_motor_collection().find_one_and_delete({ '_id': userId}) #ABCDEF find that id and delete it 
        if user is None:
            raise EntityNotFoundError
        return {'success': True, 'message': 'Delete successfully'}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success': False, 'message': enfe.message}, status_code=enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success': False,'message': str(e)}, status_code=500)
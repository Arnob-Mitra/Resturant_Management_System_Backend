from error.exception import EntityNotFoundError
from restaurant.model import Restaurant
from role.model import Role
from user.model import User
from userRole.dto import UpdateDTO, ResponseDTO
from userRole.model import UserRole
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from uuid import UUID
from pymongo import ReturnDocument
import asyncio
from utils import utils

router = APIRouter()

#@router.post('', status_code = 201)  
#async def create(data: CreateDTO):
#    try:
#        print (await asyncio.gather(User.get(data)))
#        user, role, restaurant = await asyncio.gather(User.get(data['user']), Role.get(data['role']), Restaurant.get(data['restaurant']))
#        if user is None or role is None or restaurant is None:
#            raise EntityNotFoundError
        
#        user_role = UserRole(user=user.id, role=role, restaurant=restaurant)
#        await user_role.save()
#        return{'success': True, 'message': 'User role has been created successfully', 'data': user_role}
#    except Exception as e:
#        return JSONResponse(content={'success': False, 'message': str(e)}, status_code = 500)
    
        
#@router.get('/{user_role_id}', status_code = 200)
#async def get_by_id(user_role_id:UUID):
#    try:
#        user_role = await UserRole.get(user_role_id)
#        if user_role is None:
#            raise EntityNotFoundError
#        return {'success': True, 'message': 'Successfully get the user role', 'data': ResponseDTO(**user_role.dict()).dict()}
#    except EntityNotFoundError as enfe:
#        return JSONResponse(content={'success':False, 'message': enfe.message}, status_code = enfe.status_code)
#    except Exception as e:
#        return JSONResponse(content={'success':False,'message': str(e)}, status_code = 500) 
    
    
@router.get('', status_code = 200)
async def get_all():
    try:
        user_role = await UserRole.find().to_list()
        if user_role is None:
            raise EntityNotFoundError
        return {"success": True, "message": "List of all types of user roles", 'data': user_role}
    except Exception as e:
        return JSONResponse(content={'success':False, 'message':(str(e))}, status_code = 500)
    

@router.patch('/{user_role_id}', status_code = 200)
async def update(user_role_id: UUID, data: UpdateDTO):
    try:
        doc = utils.create_update_doc(data.dict())
        user_role = await UserRole.get_motor_collection().find_one_and_update({ '_id': user_role_id}, {'$set': doc}, return_document=ReturnDocument.AFTER)
        if user_role is None:
            raise EntityNotFoundError
        return {'success':True, 'message':'User role updated successfully', 'data': user_role}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success':False, 'message': enfe.message}, status_code = enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success':False,'message': str(e)}, status_code=500)  
    
    
@router.delete('/{user_role_id}', status_code = 200)
async def delete(user_role_id:UUID):
    try: 
        user_role = await UserRole.get_motor_collection().find_one_and_delete({ '_id': user_role_id})
        if user_role is None:
            raise EntityNotFoundError
        return {'success':True, 'message':'Delete successfully'}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success': False, 'message': enfe.message}, status_code = enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success': False,'message': str(e)}, status_code = 500)       
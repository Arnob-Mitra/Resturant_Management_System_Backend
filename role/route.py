from error.exception import EntityNotFoundError
from role.dto import CreateDTO, UpdateDTO, ResponseDTO
from role.model import Role
from utils import utils
import asyncio

import asyncio
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from uuid import UUID
from pymongo import ReturnDocument

from user.model import User
from restaurant.model import Restaurant 



router = APIRouter()

@router.post('', status_code = 201)  
async def create(data: CreateDTO):
    try:
        role = Role(**data.dict())
        await role.save()
        return{'success': True, 'message': 'Role has been created successfully', 'data': role}
    except Exception as e:
        return JSONResponse(content={'success': False, 'message': str(e)}, status_code = 500)
    
        
@router.get('/{roleId}', status_code = 200)
async def get_by_id(roleId:UUID):
    try:
        role = await Role.get(roleId)
        if role is None:
            raise EntityNotFoundError
        return {'success': True, 'message': 'Successfully get the role', 'data': ResponseDTO(**role.dict()).dict()}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success':False, 'message': enfe.message}, status_code = enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success':False,'message': str(e)}, status_code = 500) 
    
    
@router.get('', status_code = 200)
async def get_all(name: str = None, admin: bool = None, restaurant: UUID = None):
    try:
        criteria = {}
        if name is not None:
            criteria['name'] = name
        if admin is not None:
            criteria['admin'] = admin
        if restaurant is not None:
            criteria['restaurant'] = restaurant  
        role = await Role.find(criteria).to_list()
        if role is None:
            raise EntityNotFoundError
        return {"success": True, "message": "List of all types of roles", 'data': role}
    except Exception as e:
        return JSONResponse(content={'success':False, 'message':(str(e))}, status_code = 500)
    

@router.patch('/{roleId}', status_code = 200)
async def update(roleId:UUID, data:UpdateDTO):
    try:
        doc = utils.create_update_doc(data.dict())
        role = await Role.get_motor_collection().find_one_and_update({ '_id': roleId}, {'$set': doc}, return_document=ReturnDocument.AFTER)
        if role is None:
            raise EntityNotFoundError
        return {'success':True, 'message':'Role updated successfully', 'data': role}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success':False, 'message': enfe.message}, status_code = enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success':False,'message': str(e)}, status_code=500)  
    
    
@router.delete('/{roleId}', status_code = 200)
async def delete(roleId:UUID):
    try: 
        role = await Role.get_motor_collection().find_one_and_delete({ '_id': roleId})
        if role is None:
            raise EntityNotFoundError
        return {'success': True, 'message': 'Delete successfully'}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success': False, 'message': enfe.message}, status_code = enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success': False,'message': str(e)}, status_code = 500)       
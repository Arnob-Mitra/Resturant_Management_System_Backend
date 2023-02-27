from error.exception import EntityNotFoundError
from userRole.dto import CreateDTO, UpdateDTO, ResponseDTO
from userRole.model import UserRole
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from uuid import UUID
from pymongo import ReturnDocument

router = APIRouter()

@router.post('/')  
async def create(data:CreateDTO):
    try:
        user_role = UserRole(**data.dict())
        await user_role.save()
        return{'success': True, 'message': 'User role has been created successfully', 'data': user_role}
    except Exception as e:
        return JSONResponse(content={'success': False, 'message': str(e)}, status_code = 500)
    
        
@router.get('/{user_roleId}')
async def get_by_id(user_roleId:UUID):
    try:
        user_role = await UserRole.get(user_roleId)
        if user_role is None:
            raise EntityNotFoundError
        return {'success':True, 'message':'Successfully get the user role', 'data':ResponseDTO(**user_role.dict()).dict()}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success':False, 'message': enfe.message}, status_code = enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success':False,'message': str(e)}, status_code = 500) 
    
    
@router.get('/')
async def get_all():
    try:
        user_role = await UserRole.find().to_list()
        if user_role is None:
            raise EntityNotFoundError
        return {"success":True, "message":"List of all types of user roles", 'data': user_role}
    except Exception as e:
        return JSONResponse(content={'success':False, 'message':(str(e))}, status_code = 500)
    

@router.patch('/{user_roleId}')
async def update(user_roleId:UUID, data:UpdateDTO):
    try:
        user_role = await UserRole.get_motor_collection().find_one_and_update({ '_id': user_roleId}, {'$set': data.dict()}, return_document=ReturnDocument.AFTER)
        if user_role is None:
            raise EntityNotFoundError
        return {'success':True, 'message':'User role updated successfully', 'data': user_role}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success':False, 'message': enfe.message}, status_code = enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success':False,'message': str(e)}, status_code=500)  
    
    
@router.delete('/{user_roleId}')
async def delete(user_roleId:UUID):
    try: 
        user_role = await UserRole.get_motor_collection().find_one_and_delete({ '_id': user_roleId})
        if user_role is None:
            raise EntityNotFoundError
        return {'success':True, 'message':'Delete successfully'}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success': False, 'message': enfe.message}, status_code = enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success': False,'message': str(e)}, status_code = 500)       
from error.exception import EntityNotFoundError
from inventory.dto import ResponseDTO, CreateDTO, UpdateDTO
from inventory.model import Inventory
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from uuid import UUID
from pymongo import ReturnDocument



router = APIRouter()

@router.post('/')  
async def create(data:CreateDTO):
    try:
        inventory = Inventory(**data.dict())
        await inventory.save()
        return{'success': True, 'message': 'Inventory has been created successfully', 'data':inventory}
    except Exception as e:
        return JSONResponse(content={'success': False, 'message': str(e)}, status_code = 500)
    
        
@router.get('/{inventoryId}')
async def get_by_id(inventoryId:UUID):
    try:
        inventory = await Inventory.get(inventoryId)
        if inventory is None:
            raise EntityNotFoundError
        return {'success':True, 'message':'Successfully get the inventory', 'data':ResponseDTO(**inventory.dict()).dict()}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success':False, 'message': enfe.message}, status_code = enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success':False,'message': str(e)}, status_code = 500) 
    
    
@router.get('/')
async def get_all():
    try:
        inventory = await Inventory.find().to_list()
        if inventory is None:
            raise EntityNotFoundError
        return {"success":True, "message":"List of all types of inventories", 'data':inventory}
    except Exception as e:
        return JSONResponse(content={'success':False, 'message':(str(e))}, status_code = 500)
    

@router.patch('/{inventoryId}')
async def update(inventoryId:UUID, data:UpdateDTO):
    try:
        inventory = await Inventory.get_motor_collection().find_one_and_update({ '_id': inventoryId}, {'$set': data.dict()}, return_document=ReturnDocument.AFTER)
        # await User.find_one(User.id == userId).update({'$set': data.dict()})
        if inventory is None:
            raise EntityNotFoundError
        return {'success':True, 'message':'Inventory updated successfully', 'data':inventory}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success':False, 'message': enfe.message}, status_code = enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success':False,'message': str(e)}, status_code=500)  
    
    
@router.delete('/{inventoryId}')
async def delete(inventoryId:UUID):
    try: 
        inventory = await Inventory.get_motor_collection().find_one_and_delete({ '_id': inventoryId})
        if inventory is None:
            raise EntityNotFoundError
        return {'success':True, 'message':'Delete successfully'}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success': False, 'message': enfe.message}, status_code = enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success': False,'message': str(e)}, status_code = 500)       
from foodItem.dto import CreateDTO, UpdateDTO, ResponseDTO
from foodItem.model import FoodItem 
from error.exception import EntityNotFoundError, Unauthorized,NotAcceptable
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from uuid import UUID
from pymongo import ReturnDocument

router = APIRouter()
    
@router.post('/')  
async def create(data:CreateDTO):
    try:
        food_item = FoodItem(**data.dict())
        await food_item.save()
        return{'success':True, 'message':'Food item successfully created', 'data':food_item}
    except Exception as e:
        return JSONResponse(content={'success':False, 'message': str(e)}, status_code = 500)
    

@router.get('/{foodId}')
async def get_by_id(foodId:UUID):
    try:
        food_item = await FoodItem.get(foodId)
        if food_item is None:
            raise EntityNotFoundError
        return {'success':True, 'message':'Successfully get the user', 'data':ResponseDTO(**food_item.dict()).dict()}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success':False, 'message': enfe.message}, status_code=enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success':False,'message': str(e)}, status_code = 500) 
    
    
@router.get('/')
async def get_all():
    try:
        food_item = await FoodItem.find().to_list()
        if food_item is None:
            raise EntityNotFoundError
        return {"success":True, "message":"List of all types of users", 'data': food_item}
    except Exception as e:
        return JSONResponse(content={'success':False, 'message':(str(e))}, status_code = 500)
    

@router.patch('/{foodId}')
async def update(foodId:UUID, data:UpdateDTO):
    try:
        food_item = await FoodItem.get_motor_collection().find_one_and_update({ '_id': foodId}, {'$set': data.dict()}, return_document=ReturnDocument.AFTER)
        if food_item is None:
            raise EntityNotFoundError
        return {'success':True, 'message':'User updated successfully', 'data':food_item}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success':False, 'message': enfe.message}, status_code=enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success':False,'message': str(e)}, status_code=500)  
    
    
@router.delete('/{foodId}')
async def delete(foodId:UUID):
    try: 
        food_item = await FoodItem.get_motor_collection().find_one_and_delete({ '_id': foodId})
        if food_item is None:
            raise EntityNotFoundError
        return {'success':True, 'message':'Delete successfully'}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success': False, 'message': enfe.message}, status_code = enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success': False,'message': str(e)}, status_code = 500)
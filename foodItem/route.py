from foodItem.dto import CreateDTO, UpdateDTO, ResponseDTO
from foodItem.model import FoodItem 
from error.exception import EntityNotFoundError
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from uuid import UUID
from pymongo import ReturnDocument

router = APIRouter()
    
@router.post('', status_code=201)  
async def create(data:CreateDTO):
    try:
        food_item = FoodItem(**data.dict())
        await food_item.save()
        return{'success':True, 'message':'Food item successfully created', 'data':food_item}
    except Exception as e:
        return JSONResponse(content={'success':False, 'message': str(e)}, status_code = 500)
    

@router.get('/{foodId}', status_code=200)
async def get_by_id(foodId:UUID):
    try:
        food_item = await FoodItem.get(foodId)
        if food_item is None:
            raise EntityNotFoundError
        return {'success':True, 'message':'Successfully get the food item', 'data':ResponseDTO(**food_item.dict()).dict()}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success':False, 'message': enfe.message}, status_code=enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success':False,'message': str(e)}, status_code = 500) 
    
    
@router.get('', status_code=200)
async def get_all(name: str = None, category: str = None, subcategory: str = None, cuisine: str = None):
    try:
        critetia = {}
        if name is not None:
            critetia['name'] = name
        if category is not None:
            critetia['category'] = category
        if subcategory is not None:
            critetia['subcategory'] = subcategory
        if cuisine is not None:
            critetia['cuisine'] = cuisine            
        food_item = await FoodItem.find(critetia).to_list()
        if food_item is None:
            raise EntityNotFoundError
        return {"success":True, "message":"List of all types of food items", 'data': food_item}
    except Exception as e:
        return JSONResponse(content={'success':False, 'message':(str(e))}, status_code = 500)
    

@router.patch('/{foodId}', status_code=200)
async def update(foodId:UUID, data:UpdateDTO):
    try:
        food_item = await FoodItem.get_motor_collection().find_one_and_update({ '_id': foodId}, {'$set': data.dict()}, return_document=ReturnDocument.AFTER)
        if food_item is None:
            raise EntityNotFoundError
        return {'success':True, 'message':'Food items updated successfully', 'data':food_item}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success':False, 'message': enfe.message}, status_code=enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success':False,'message': str(e)}, status_code=500)  
    
    
@router.delete('/{foodId}', status_code=200)
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
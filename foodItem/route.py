from foodItem.dto import CreateDTO, UpdateDTO, ResponseDTO
from foodItem.model import FoodItem as foodModel
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from uuid import UUID

router = APIRouter()

@router.post('/')
async def create(data:CreateDTO):
    try:
        food_item = foodModel(**data.dict())
        await food_item.save()
        return{'success':True, 'message':'Food item successfully created', 'data':food_item}
    except Exception as e:
        return JSONResponse (content={'success':False, 'message': str(e)}, status_code=500)

@router.get('/{foodId}')
async def get_by_id(foodId:UUID):
    data = await foodModel.get(foodId)
    return {'success':True, 'message':'Successfully get the food item'}
    
@router.get('/')
async def get_all():
    data = await foodModel.find().to_list()
    return {"success":True, "message":"List of all food items", 'data':data}

@router.patch('/{foodId}')
async def update(foodId:UUID, data:UpdateDTO):
    result = await foodModel.find_one(foodModel.id == foodId).update({'$set': data.dict()})
    return {'success':True, 'message':'Food item updated successfully', 'data': data.dict()}

@router.delete('/{foodId}')
async def delete(foodId:UUID):
    data = await foodModel.find_one(foodModel.id == foodId).delete()
    return {'success':True, 'message':'Food item delate successfully', 'data':data}
from foodItem.dto import FoodItemDTO as foodDTO
from foodItem.model import FoodItem as foodModel
from fastapi import APIRouter
from uuid import UUID

router = APIRouter()

@router.get('/{foodId}')
async def get_by_id(foodId:UUID):
    data = await foodModel.get(foodId)
    return {'success':True, 'message':'Successfully get the food item'}
    
@router.get('/')
async def get_all():
    data = await foodModel.find().to_list()
    return {"success":True, "message":"List of all food items", 'data':data}

@router.post('/')
async def create(data:foodDTO):
    food_item = foodModel(**data.dict())
    await food_item.save()
    return{'success':True, 'message':'Food item successfully created', 'data':food_item}


@router.patch('/{foodId}')
async def update(foodId:UUID, data:foodDTO):
    result = await foodModel.find_one(foodModel.id == foodId).update({'$set': data.dict()})
    return {'success':True, 'message':'Food item updated successfully', 'data': data.dict()}

@router.delete('/{foodId}')
async def delete(foodId:UUID, data:foodDTO):
    data = await foodModel.find_one(foodModel.id == foodId).delete()
    return {'success':True, 'message':'Food item delate successfully', 'data':data}
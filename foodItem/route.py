from foodItem.dto import FoodItemDTO as foodDTO
from foodItem.model import FoodItem as foodModel
from fastapi import APIRouter
from uuid import UUID

router = APIRouter()

@router.get('/')
async def getfoodItem():
    return{"Successfully get the food item"}

@router.get('/getFoodItemByName')
async def getByName(name:str):
    data = await foodModel.find_one(foodModel.name == name)
    return {'success':True, 'message':'Successfully get the food item', 'data': data}
    
@router.get('/all')
async def getAll():
    data = await foodModel.find().to_list()
    return {"success":True, "message":"List of all food items", 'data':data}

@router.post('/fooditem')
async def foodItem(data:foodDTO):
    food_item = foodModel(**data.dict())
    await food_item.save()
    return{'success':True, 'message':'Food item successfully created', 'data':food_item}


@router.patch('/updateFoodItem/{foodId}')
async def FoodItemUpdate(foodId:UUID, data:foodDTO):
    result = await foodModel.find_one(foodModel.id == foodId).update({'$set': data.dict()})
    return {'success':True, 'message':'Food item updated successfully', 'data': data.dict()}

@router.delete('/deleteFoodItem/{foodId}')
async def FoodItemDelete(foodId:UUID, data:foodDTO):
    data = await foodModel.find_one(foodModel.id == foodId)
    await data.delete()
    return {'success':True, 'message':'Food item delate successfully', 'data':data}
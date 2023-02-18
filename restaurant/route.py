from restaurant.dto import RestaurantDTO 
from restaurant.model import Restaurant
from fastapi import APIRouter
from uuid import UUID

router = APIRouter()

@router.get('/{restaurantId}')
async def get_by_id(restaurantId:UUID):
    data = await Restaurant.get(restaurantId)
    return {'success':True, 'message':'Successfully get the restaurant'}


@router.get('/')
async def get_all():
    data = await Restaurant.find().to_list()
    return {"success":True, "message":"List of all food items", 'data':data}


@router.post('/')
async def create(data:RestaurantDTO):
    result = Restaurant(**data.dict())
    await result.save()
    return{'success':True, 'message':'Food item successfully created', 'data':result}


@router.patch('/{restaurantId}')
async def update(restaurantId:UUID, data:RestaurantDTO):
    result = await Restaurant.find_one(Restaurant.id == restaurantId).update({'$set': data.dict()})
    return {'success':True, 'message':'Food item updated successfully', 'data': data.dict()}

@router.delete('/{restaurantId}')
async def delete(restaurantId:UUID, data:RestaurantDTO):
    data = await Restaurant.find_one(Restaurant.id == restaurantId).delete()
    return {'success':True, 'message':'Food item delate successfully', 'data':data}
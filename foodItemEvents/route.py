from foodItemEvents.createdto import FoodItemEventsDTO
from foodItemEvents.model import FoodItemEvents
from fastapi import APIRouter
from uuid import UUID

router = APIRouter()

@router.get('/{eventsId}')
async def get_by_id(eventsId:UUID):
    data = await FoodItemEvents.get(eventsId)
    return {'success':True, 'message':'Successfully get the food item events'}
    
@router.get('/')
async def get_all():
    data = await FoodItemEvents.find().to_list()
    return {"success":True, "message":"List of all food item events", 'data':data}

@router.post('/')
async def create(data:FoodItemEventsDTO):
    data = FoodItemEvents(**data.dict())
    await data.save()
    return{'success':True, 'message':'Food item events successfully created', 'data':data}


@router.patch('/{eventsId}')
async def update(eventsId:UUID, data:FoodItemEventsDTO):
    result = await FoodItemEvents.find_one(FoodItemEvents.id == eventsId).update({'$set': data.dict()})
    return {'success':True, 'message':'Food item events updated successfully', 'data': data.dict()}

@router.delete('/{eventsId}')
async def delete(eventsId:UUID, data:FoodItemEventsDTO):
    data = await FoodItemEvents.find_one(FoodItemEvents.id == eventsId).delete()
    return {'success':True, 'message':'Food item events delate successfully', 'data':data}
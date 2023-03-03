from restaurant.dto import CreateDTO, UpdateDTO, ResponseDTO
from restaurant.model import Restaurant, ModeEnum
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from error.exception import EntityNotFoundError
from uuid import UUID
from pymongo import ReturnDocument

router = APIRouter()

@router.post('', status_code=201)
async def create(data:CreateDTO):
    try: 
        restaurant = Restaurant(**data.dict())
        await restaurant.save()
        return{'success': True, 'message':'Restaurant successfully created', 'data': restaurant}
    except Exception as e:
        return JSONResponse(content={'success':False, 'message':str(e)}, status_code = 500) 
    
    
@router.get('/{restaurantId}', status_code=200)
async def get_by_id(restaurantId:UUID):
    try:
        restaurant = await Restaurant.get(restaurantId)
        if restaurant is None:
            return EntityNotFoundError
        return {'success': True, 'message': 'Successfully get the restaurant', 'data': ResponseDTO(**restaurant.dict()).dict()}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success':False, 'message': enfe.message}, status_code=enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success':False,'message': str(e)}, status_code=500)


@router.get('', status_code=200)
async def get_all(name: str = None, mode: ModeEnum = None):
    try:
        criteria = {}
        if name is not None:
            criteria['name'] = name    
        if mode is not None:
            criteria['mode'] = mode               
        restuarant = await Restaurant.find(criteria).to_list()
        if restuarant is None:
            return EntityNotFoundError
        return {"success":True, "message":"List of all restaurants", 'data':restuarant}
    except Exception as e:
        return JSONResponse(content={'success':False, 'message':str(e)}, status_code=500)


@router.patch('/{restaurantId}', status_code=200)
async def update(restaurantId:UUID, data:UpdateDTO):
    try:
        restaurant = await Restaurant.get_motor_collection().find_one_and_update({ '_id': restaurantId}, {'$set': data.dict()}, return_document=ReturnDocument.AFTER)
        if restaurant is None:
            raise EntityNotFoundError
        return {'success':True, 'message':'Restaurant updated successfully', 'data': data.dict()}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success':False, 'message': enfe.message}, status_code=enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success':False,'message': str(e)}, status_code=500)
    

@router.delete('/{restaurantId}', status_code=200)
async def delete(restaurantId:UUID):
    try:
        restuarant = await Restaurant.get_motor_collection().find_one_and_delete({'_id':restaurantId})
        if restuarant is None:
            raise EntityNotFoundError
        return {'success':True, 'message':'Restaurant delate successfully'}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success':False, 'message':enfe.message}, status_code=enfe.status_code)
    except Exception as e:
        return JSONResponse(content= {'success':False, 'message':str(e)}, status_code=500)
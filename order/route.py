from error.exception import EntityNotFoundError
from order.dto import CreateDTO, UpdateDTO, ResponseDTO
from order.model import Order, OrderStatusEnum, FoodItem
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from uuid import UUID
from pymongo import ReturnDocument
from restaurant.model import Restaurant
from beanie import Link

router = APIRouter()

@router.post('', status_code=201)  
async def create(data:CreateDTO):
    try:
        order = Order(**data.dict())
        await order.save()
        return{'success': True, 'message': 'Order has been created successfully', 'data': order}
    except Exception as e:
        return JSONResponse(content={'success': False, 'message': str(e)}, status_code = 500)
    
        
@router.get('/{orderId}', status_code=200)
async def get_by_id(orderId:UUID):
    try:
        order = await Order.get(orderId)
        print(order)
        if order is None:
            raise EntityNotFoundError
        return {'success':True, 'message':'Successfully get the order', 'data':ResponseDTO(**order.dict()).dict()}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success':False, 'message': enfe.message}, status_code = enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success':False,'message': str(e)}, status_code = 500) 
    
    
@router.get('', status_code=200)
async def get_all(food_items: FoodItem = None, status: OrderStatusEnum = None, table_number: str = None):
    try:
        criteria = {}
        if food_items is not None:
            criteria['food_items'] = food_items
        if status is not None:
            criteria['status'] = status
        if table_number is not None:
            criteria['table_number'] = table_number           
        order = await Order.find(criteria).to_list()
        if order is None:
            raise EntityNotFoundError
        return {"success":True, "message":"List of all orders", 'data': order}
    except Exception as e:
        return JSONResponse(content={'success':False, 'message':(str(e))}, status_code = 500)
    

@router.patch('/{orderId}', status_code=200)
async def update(orderId:UUID, data:UpdateDTO):
    try:
        order = await Order.get_motor_collection().find_one_and_update({ '_id': orderId}, {'$set': data.dict()}, return_document=ReturnDocument.AFTER)
        if order is None:
            raise EntityNotFoundError
        return {'success':True, 'message':'Order updated successfully', 'data': order}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success':False, 'message': enfe.message}, status_code = enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success':False,'message': str(e)}, status_code=500)  
    
    
@router.delete('/{orderId}', status_code=200)
async def delete(orderId:UUID):
    try: 
        order = await Order.get_motor_collection().find_one_and_delete({ '_id': orderId})
        if order is None:
            raise EntityNotFoundError
        return {'success':True, 'message':'Delete successfully'}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success': False, 'message': enfe.message}, status_code = enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success': False,'message': str(e)}, status_code = 500)   
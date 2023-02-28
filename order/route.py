from error.exception import EntityNotFoundError
from order.dto import CreateDTO, UpdateDTO, ResponseDTO
from order.model import Order
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from uuid import UUID
from pymongo import ReturnDocument

router = APIRouter()

@router.post('/')  
async def create(data:CreateDTO):
    try:
        order = Order(**data.dict())
        await order.save()
        return{'success': True, 'message': 'Order has been created successfully', 'data': order}
    except Exception as e:
        return JSONResponse(content={'success': False, 'message': str(e)}, status_code = 500)
    
        
@router.get('/{orderId}')
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
    
    
@router.get('/')
async def get_all():
    try:
        order = await Order.find().to_list()
        if order is None:
            raise EntityNotFoundError
        return {"success":True, "message":"List of all orders", 'data': order}
    except Exception as e:
        return JSONResponse(content={'success':False, 'message':(str(e))}, status_code = 500)
    

@router.patch('/{orderId}')
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
    
    
@router.delete('/{orderId}')
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
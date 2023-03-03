from error.exception import EntityNotFoundError
from orderEvent.dto import CreateDTO, UpdateDTO, ResponseDTO
from orderEvent.model import OrderEvent
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from uuid import UUID
from pymongo import ReturnDocument

router = APIRouter()

@router.post('', status_code = 201)  
async def create(data:CreateDTO):
    try:
        order_event = OrderEvent(**data.dict())
        await order_event.save()
        return{'success': True, 'message': 'Order Event has been created successfully', 'data': order_event}
    except Exception as e:
        return JSONResponse(content={'success': False, 'message': str(e)}, status_code = 500)
    
        
@router.get('/{order_eventId}', status_code = 200)
async def get_by_id(order_eventId:UUID):
    try:
        order_event = await OrderEvent.get(order_eventId)
        if order_event is None:
            raise EntityNotFoundError
        return {'success':True, 'message':'Successfully get the order event', 'data':ResponseDTO(**order_event.dict()).dict()}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success':False, 'message': enfe.message}, status_code = enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success':False,'message': str(e)}, status_code = 500) 
    
    
@router.get('', status_code = 200)
async def get_all():
    try:
        order_event = await OrderEvent.find().to_list()
        if order_event is None:
            raise EntityNotFoundError
        return {"success":True, "message":"List of all order events", 'data': order_event}
    except Exception as e:
        return JSONResponse(content={'success':False, 'message':(str(e))}, status_code = 500)
    

@router.patch('/{order_eventId}', status_code = 200)
async def update(order_eventId:UUID, data:UpdateDTO):
    try:
        order_event = await OrderEvent.get_motor_collection().find_one_and_update({ '_id': order_eventId}, {'$set': data.dict()}, return_document=ReturnDocument.AFTER)
        if order_event is None:
            raise EntityNotFoundError
        return {'success':True, 'message':'Order event updated successfully', 'data': order_event}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success':False, 'message': enfe.message}, status_code = enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success':False,'message': str(e)}, status_code=500)  
    
    
@router.delete('/{order_eventId}', status_code = 200)
async def delete(order_eventId:UUID):
    try: 
        order_event = await OrderEvent.get_motor_collection().find_one_and_delete({ '_id': order_eventId})
        if order_event is None:
            raise EntityNotFoundError
        return {'success':True, 'message':'Delete successfully'}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success': False, 'message': enfe.message}, status_code = enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success': False,'message': str(e)}, status_code = 500)   
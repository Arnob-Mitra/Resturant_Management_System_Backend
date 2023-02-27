from error.exception import EntityNotFoundError
from floorPlan.dto import CreateDTO, UpdateDTO, ResponseDTO
from floorPlan.model import FloorPlan
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from uuid import UUID
from pymongo import ReturnDocument

router = APIRouter()

@router.post('/')  
async def create(data:CreateDTO):
    try:
        floor_plan = FloorPlan(**data.dict())
        await floor_plan.save()
        return{'success': True, 'message': 'Floor plan has been created successfully', 'data':floor_plan}
    except Exception as e:
        return JSONResponse(content={'success': False, 'message': str(e)}, status_code = 500)
    
        
@router.get('/{floorId}')
async def get_by_id(floorId:UUID):
    try:
        floor_plan = await FloorPlan.get(floorId)
        if floor_plan is None:
            raise EntityNotFoundError
        return {'success':True, 'message':'Successfully get the floor plan', 'data':ResponseDTO(**floor_plan.dict()).dict()}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success':False, 'message': enfe.message}, status_code = enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success':False,'message': str(e)}, status_code = 500) 
    
    
@router.get('/')
async def get_all():
    try:
        floor_plan = await FloorPlan.find().to_list()
        if floor_plan is None:
            raise EntityNotFoundError
        return {"success":True, "message":"List of all types of floor plans", 'data':floor_plan}
    except Exception as e:
        return JSONResponse(content={'success':False, 'message':(str(e))}, status_code = 500)
    

@router.patch('/{floorId}')
async def update(floorId:UUID, data:UpdateDTO):
    try:
        floor_plan = await FloorPlan.get_motor_collection().find_one_and_update({ '_id': floorId}, {'$set': data.dict()}, return_document=ReturnDocument.AFTER)
        if floor_plan is None:
            raise EntityNotFoundError
        return {'success':True, 'message':'Floor plan updated successfully', 'data': floor_plan}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success':False, 'message': enfe.message}, status_code = enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success':False,'message': str(e)}, status_code=500)  
    
    
@router.delete('/{floorId}')
async def delete(floorId:UUID):
    try: 
        floor_plan = await FloorPlan.get_motor_collection().find_one_and_delete({ '_id': floorId})
        if floor_plan is None:
            raise EntityNotFoundError
        return {'success':True, 'message':'Delete successfully'}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success': False, 'message': enfe.message}, status_code = enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success': False,'message': str(e)}, status_code = 500)       
from floorPlan.dto import CreateDTO, UpdateDTO, ResponseDTO
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from floorPlan.model import FloorPlan
from error.exception import EntityNotFoundError
from uuid import UUID
from restaurant.model import Restaurant

router = APIRouter()

@router.post('/')
async def create(data:CreateDTO):
    try: 
        floor_plan = FloorPlan(**data.dict())
        await floor_plan.save()
        return{'success':True, 'message':'Food item successfully created', 'data':floor_plan}
    except Exception as e:
        return JSONResponse(content={'success':False, 'message':str(e)}, status_code = 500) 
    
@router.get('/{restaurantId}')
async def get_by_id(restaurantId:UUID):
    try:
        restaurant = await Restaurant.get(restaurantId)
        if restaurant is None:
            return EntityNotFoundError
        return {'success':True, 'message':'Successfully get the restaurant', 'data':ResponseDTO(**restaurant.dict()).dict()}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success':False, 'message': enfe.message}, status_code=enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success':False,'message': str(e)}, status_code=500)
 
@router.get('/')
async def get_all():
    try:
        floor_plan = await FloorPlan.find().to_list()   
        if floor_plan is None:
            return EntityNotFoundError
        return{'success': True, 'message': 'List of all floor plan', 'data':- floor_plan}
    except Exception as e:
        return JSONResponse (content = {'success': False, 'message': str(e)}, status_code = 500)
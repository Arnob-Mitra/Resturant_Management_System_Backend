from error.exception import EntityNotFoundError
from rating.dto import CreateDTO, UpdateDTO, ResponseDTO
from rating.model import Rating, RatingEnum
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from uuid import UUID
from pymongo import ReturnDocument

router = APIRouter()

@router.post('', status_code=201)  
async def create(data:CreateDTO):
    try:
        rating = Rating(**data.dict())
        await rating.save()
        return{'success': True, 'message': 'Rating has been created successfully', 'data': rating}
    except Exception as e:
        return JSONResponse(content={'success': False, 'message': str(e)}, status_code = 500)
    
        
@router.get('/{ratingId}', status_code = 200)
async def get_by_id(ratingId:UUID):
    try:
        rating = await Rating.get(ratingId)
        if rating is None:
            raise EntityNotFoundError
        return {'success':True, 'message':'Successfully get the rating', 'data':ResponseDTO(**rating.dict()).dict()}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success':False, 'message': enfe.message}, status_code = enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success':False,'message': str(e)}, status_code = 500) 
    
    
@router.get('', status_code = 200)
async def get_all(ambience: RatingEnum = None, taste: RatingEnum = None, cleanliness: RatingEnum = None, staff: RatingEnum = None, budget_friendly: RatingEnum = None,):
    try:
        criteria = {}
        if ambience is not None:
            criteria['ambience'] = ambience
        if taste is not None:
            criteria['taste'] = taste
        if cleanliness is not None:
            criteria['cleanliness'] = cleanliness
        if staff is not None:
            criteria['staff'] = staff
        if budget_friendly is not None:
            criteria['budget_friendly'] = budget_friendly                
        rating = await Rating.find(criteria).to_list()
        if rating is None:
            raise EntityNotFoundError
        return {"success":True, "message":"List of all types of ratings", 'data': rating}
    except Exception as e:
        return JSONResponse(content={'success':False, 'message':(str(e))}, status_code = 500)
    

@router.patch('/{ratingId}', status_code = 200)
async def update(ratingId:UUID, data:UpdateDTO):
    try:
        rating = await Rating.get_motor_collection().find_one_and_update({ '_id': ratingId}, {'$set': data.dict()}, return_document=ReturnDocument.AFTER)
        # await User.find_one(User.id == userId).update({'$set': data.dict()})
        if rating is None:
            raise EntityNotFoundError
        return {'success':True, 'message':'Rating updated successfully', 'data': rating}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success':False, 'message': enfe.message}, status_code = enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success':False,'message': str(e)}, status_code=500)  
    
    
@router.delete('/{ratingId}', status_code = 200)
async def delete(ratingId:UUID):
    try: 
        rating = await Rating.get_motor_collection().find_one_and_delete({ '_id': ratingId})
        if rating is None:
            raise EntityNotFoundError
        return {'success':True, 'message':'Delete successfully'}
    except EntityNotFoundError as enfe:
        return JSONResponse(content={'success': False, 'message': enfe.message}, status_code = enfe.status_code)
    except Exception as e:
        return JSONResponse(content={'success': False,'message': str(e)}, status_code = 500)       
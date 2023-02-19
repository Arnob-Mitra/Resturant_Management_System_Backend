from user.createdto import UserDTO
from user.model import User
from fastapi import APIRouter
from uuid import UUID

router = APIRouter()

@router.get('/{userId}')
async def get_by_id(userId:UUID):
    data = await User.get(userId)
    return {'success':True, 'message':'Successfully get the user'}
    
@router.get('/')
async def get_all():
    data = await User.find().to_list()
    return {"success":True, "message":"List of all users", 'data':data}

@router.post('/')
async def create(data:UserDTO):
    data = User(**data.dict())
    await data.save()
    return{'success':True, 'message':'User successfully created', 'data':data}


@router.patch('/{userId}')
async def update(userId:UUID, data:UserDTO):
    result = await User.find_one(User.id == userId).update({'$set': data.dict()})
    return {'success':True, 'message':'User updated successfully', 'data': data.dict()}

@router.delete('/{userId}')
async def delete(userId:UUID, data:UserDTO):
    data = await User.find_one(User.id == userId).delete()
    return {'success':True, 'message':'User delate successfully', 'data':data}
from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import mongodb

from foodItem.route import router as fooditemRouter
from middleware.main import AuthorizationMiddleware
from restaurant.route import router as restaurantRouter
from user.route import router as userRouter
from floorPlan.route import router as floorplanRouter
from inventory.route import router as inventoryRouter
from order.route import router as orderRouter
from orderEvent.route import router as orderEventRouter
from rating.route import router as ratingRouter
from role.route import router as roleRouter
from userRole.route import router as userRoleRouter

load_dotenv()

app = FastAPI()

endpoints = [{
    'method': 'POST',
    'regex': r'^\/user\/login$',
  }, {
    'method': 'POST',
    'regex': r'^\/user$',
  },{
    'method': 'PATCH',
    'regex': r'^\/user\/cha\/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$',
  },
]
app.add_middleware(AuthorizationMiddleware, skip_endpoints=endpoints)

module_api_path = '/api/v1'
app.include_router(fooditemRouter, prefix=module_api_path+'/fooditem')
app.include_router(restaurantRouter, prefix=module_api_path+'/restaurant')
app.include_router(userRouter, prefix=module_api_path+'/user')
app.include_router(floorplanRouter, prefix=module_api_path+'/floorplan')
app.include_router(inventoryRouter, prefix=module_api_path+'/inventory')
app.include_router(orderRouter, prefix=module_api_path+'/order')
app.include_router(orderEventRouter, prefix=module_api_path+'/orderevent')
app.include_router(ratingRouter, prefix=module_api_path+'/rating')
app.include_router(roleRouter, prefix=module_api_path+'/role')
app.include_router(userRoleRouter, prefix=module_api_path+'/userRole')

app.add_middleware(
  CORSMiddleware, 
  allow_origins=['*'], 
  allow_methods=['*'], 
  allow_headers=['*'], 
  allow_credentials=True
)

@app.on_event('startup')
async def start_db():
  await mongodb.init()
from fastapi import FastAPI
from foodItem.route import router as fooditemRouter
from restaurant.route import router as restaurantRouter
from user.route import router as userRouter
from floorPlan.route import router as floorplanRouter
from inventory.route import router as inventoryRouter
from order.route import router as orderRouter
from orderEvent.route import router as orderEventRouter
from rating.route import router as ratingRouter
from role.route import router as roleRouter
from userRole.route import router as userRoleRouter
from database import mongodb


app = FastAPI()
app.include_router(fooditemRouter, prefix='/fooditem')
app.include_router(restaurantRouter, prefix='/restaurant')
app.include_router(userRouter, prefix='/user')
app.include_router(floorplanRouter, prefix='/floorplan')
app.include_router(inventoryRouter, prefix='/inventory')
app.include_router(orderRouter, prefix='/order')
app.include_router(orderEventRouter, prefix='/orderevent')
app.include_router(ratingRouter, prefix='/rating')
app.include_router(roleRouter, prefix='/role')
app.include_router(userRoleRouter, prefix='/userRole')


@app.on_event('startup')
async def start_db():
  await mongodb.init()
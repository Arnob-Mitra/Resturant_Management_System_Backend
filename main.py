from fastapi import FastAPI
from foodItem.route import router as fooditemRouter
from restaurant.route import router as restaurantRouter
from foodItemEvents.route import router as fooditemeventsRouter
from user.route import router as userRouter
from floorPlan.route import router as floorplanRouter
from database import mongodb

app = FastAPI()
app.include_router(fooditemRouter, prefix='/fooditem')
app.include_router(restaurantRouter, prefix='/restaurant')
app.include_router(fooditemeventsRouter, prefix='/fooditemevents')
app.include_router(userRouter, prefix='/user')
app.include_router(floorplanRouter, prefix='/floorplan')

@app.on_event('startup')
async def start_db():
  await mongodb.init()
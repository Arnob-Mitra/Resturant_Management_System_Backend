from fastapi import FastAPI
from foodItem.route import router as fooditemRouter
from restaurant.route import router as restaurantRouter
from database import mongodb

app = FastAPI()
app.include_router(fooditemRouter, prefix='/fooditem')
app.include_router(restaurantRouter, prefix='/restaurant')


@app.on_event('startup')
async def start_db():
  await mongodb.init()
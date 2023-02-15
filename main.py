from fastapi import FastAPI
from foodItem.route import router as fooditemRouter
from database import mongodb

app = FastAPI()
app.include_router(fooditemRouter, prefix='/fooditem')

@app.on_event('startup')
async def start_db():
  await mongodb.init()
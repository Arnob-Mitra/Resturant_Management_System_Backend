from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

async def init():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    print(await client.server_info()) 
    await init_beanie(database=client['rms'], document_models=["foodItem.model.FoodItem"])
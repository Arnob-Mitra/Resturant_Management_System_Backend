import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie


async def init():
    client = AsyncIOMotorClient("mongodb+srv://ripasarkar:GNqmhvQfXb3DePvM@cluster0.qhvvzf0.mongodb.net/?retryWrites=true&w=majority")
    print(await client.server_info()) 
    await init_beanie(database=client['rms'], document_models=["foodItem.model.FoodItem", "restaurant.model.Restaurant"])

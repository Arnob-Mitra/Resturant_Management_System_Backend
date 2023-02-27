import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie


async def init():
    client = AsyncIOMotorClient("mongodb+srv://ripasarkar01:ljrKV8JOuO9vHLWt@cluster0.njzpo0l.mongodb.net/?retryWrites=true&w=majority", uuidRepresentation='standard')
    #print(await client.server_info()) 
    await init_beanie(database=client['rms'], document_models=["foodItem.model.FoodItem", "restaurant.model.Restaurant", "user.model.User","floorPlan.model.FloorPlan","inventory.model.Inventory","order.model.Order","orderEvent.model.OrderEvent","userRole.model.UserRole","role.model.Role","rating.model.Rating"])

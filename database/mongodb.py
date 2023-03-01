import os

from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
import certifi

from error.exception import ImproperConfigurationError


async def init():
    conn_params = {
        'host': os.environ.get('MONGODB_HOST', None),
        'username': os.environ.get('MONGODB_USER', None),
        'password': os.environ.get('MONGODB_PASS', None),
    }
    
    if all(conn_params.values()):
        #ABCDEF must expose it to all models or routes by settings file
        client: AsyncIOMotorClient = AsyncIOMotorClient(
        host=conn_params['host'],
            username=conn_params['username'],
            password=conn_params['password'],
            uuidRepresentation='standard',
            tlsCAFile=certifi.where()
        )

        print(await client.server_info())
    else:
        raise ImproperConfigurationError
    
    db_name = os.environ.get('MONGODB_DATABASE', None)
    if db_name is not None:
        await init_beanie(database=client[db_name], document_models=[
            "foodItem.model.FoodItem", 
            "restaurant.model.Restaurant",
            "user.model.User",
            "floorPlan.model.FloorPlan",
            "inventory.model.Inventory"
        ])
    else:
        raise ImproperConfigurationError

from motor.motor_asyncio import AsyncIOMotorClient
from db_conf import MONGO_URL


mongo_db = AsyncIOMotorClient(MONGO_URL)






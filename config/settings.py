import os
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv("config/.env")

MONGO_URL = os.getenv("MONGO_URL")
MONGO_DB = os.getenv("MONGO_DB")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")


client = AsyncIOMotorClient(MONGO_URL)

db = client[MONGO_DB]

employee_collection = db.get_collection(MONGO_COLLECTION)


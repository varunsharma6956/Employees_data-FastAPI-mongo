from fastapi import APIRouter
import traceback
from bson import ObjectId
from fastapi.responses import JSONResponse
from config.settings import employee_collection
import json

get_employee_router = APIRouter()

@get_employee_router.get("/employees")
async def get_employee():
    try:
        # make query
        employees = await employee_collection.find({}).to_list(length=None)

        # Convert ObjectId to string in the response
        for employee in employees:
            employee["_id"] = str(employee["_id"])

        return JSONResponse(content={"data": employees}, status_code=200)
    except Exception as e:
        traceback.print_exc()
        return JSONResponse(
            content={"message": "Internal server error"},
            status_code=500
        )
    


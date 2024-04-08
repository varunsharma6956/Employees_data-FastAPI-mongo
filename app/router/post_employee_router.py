from fastapi import APIRouter, HTTPException
import traceback
from bson import ObjectId
from fastapi.responses import JSONResponse
from config.settings import employee_collection
import json

post_employee_router = APIRouter()

# POST operation to create a new employee
@post_employee_router.post("/employees")
async def create_employee(employee_data: dict):
    try:
        # Insert the new employee data into the collection
        result = await employee_collection.insert_one(employee_data)
        new_employee_id = str(result.inserted_id)
        return JSONResponse(content={"message": "Employee created successfully", "employee_id": new_employee_id}, status_code=201)
    except Exception as e:
        traceback.print_exc()
        return JSONResponse(content={"message": "Internal server error"}, status_code=500)
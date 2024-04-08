from fastapi import APIRouter, HTTPException, Query
import traceback
from bson import ObjectId
from fastapi.responses import JSONResponse
from config.settings import employee_collection
import json

update_employee_router = APIRouter()

# PATCH operation to update an existing employee
@update_employee_router.patch("/employees")
async def update_employee(employee_id: str, updated_employee_data: dict):
    try:
        # Retrieve the existing employee data
        existing_employee = await employee_collection.find_one({"_id": ObjectId(employee_id)})
        if existing_employee is None:
            return JSONResponse(content={"message": "Employee not found"}, status_code=404)

        # Update the existing employee data with the provided data
        updated_employee = {**existing_employee, **updated_employee_data}

        # Update the employee data in the collection
        result = await employee_collection.update_one({"_id": ObjectId(employee_id)}, {"$set": updated_employee})
        
        if result.modified_count == 1:
            return JSONResponse(content={"message": "Employee updated successfully"}, status_code=200)
        else:
            return JSONResponse(content={"message": "Employee not found"}, status_code=404)
    except Exception as e:
        traceback.print_exc()
        return JSONResponse(content={"message": "Internal server error"}, status_code=500)















'''from fastapi import APIRouter, HTTPException
import traceback
from bson import ObjectId
from fastapi.responses import JSONResponse
from config.settings import employee_collection
import json

update_employee_router = APIRouter()

# UPDATE operation to update an existing employee
@update_employee_router.patch("/employees")
async def update_employee(employee_id: str, updated_employee_data: dict):
    try:
        # Update the employee data in the collection
        print(employee_id)
        result = await employee_collection.update_one({"_id": ObjectId(employee_id)}, 
        {"$set": updated_employee_data})
        if result.modified_count == 1:
            return JSONResponse(content={"message": "Employee updated successfully"}, status_code=200)
        else:
            return JSONResponse(content={"message": "Employee not found"}, status_code=404)
    except Exception as e:
        traceback.print_exc()
        return JSONResponse(content={"message": "Internal server error"}, status_code=500)

        '''
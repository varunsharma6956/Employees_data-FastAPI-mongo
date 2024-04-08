from fastapi import APIRouter, HTTPException, Query, Body
import traceback
from bson import ObjectId
from fastapi.responses import JSONResponse
from config.settings import employee_collection
from pydantic import BaseModel  # Importing Pydantic's BaseModel for defining request/response models

put_employee_router = APIRouter()

class EmployeeUpdate(BaseModel):  # Define Pydantic model for the employee update request body
    name: str
    designation: str
    department: str

# PUT operation to update an existing employee
@put_employee_router.put("/employees")
async def update_employee(employee_id: str, employee_data: dict=Body()):
    try:
        # Convert employee_id to ObjectId
        obj_id = ObjectId(employee_id)
        
        # Update the employee data in the collection
        result = await employee_collection.update_one({"_id": obj_id}, {"$set": employee_data})
        
        # Check if the employee exists
        if result.modified_count == 0:
            return JSONResponse(content={"message": "Employee not found"}, status_code=404)
        
        return JSONResponse(content={"message": "Employee updated successfully"}, status_code=200)
    except Exception as e:
        traceback.print_exc()
        return JSONResponse(content={"message": "Internal server error"}, status_code=500)

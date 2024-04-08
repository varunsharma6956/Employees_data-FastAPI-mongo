from fastapi import APIRouter, HTTPException
import traceback
from bson import ObjectId
from fastapi.responses import JSONResponse
from config.settings import employee_collection
import json

delete_employee_router = APIRouter()

# DELETE operation to delete an employee
@delete_employee_router.delete("/employees")
async def delete_employee(employee_id: str):
    try:
        # Delete the employee from the collection
        result = await employee_collection.delete_one({"_id": ObjectId(employee_id)})
        if result.deleted_count == 1:
            return JSONResponse(content={"message": "Employee deleted successfully"}, status_code=200)
        else:
            return JSONResponse(content={"message": "Employee not found"}, status_code=404)
    except Exception as e:
        traceback.print_exc()
        return JSONResponse(content={"message": "Internal server error"}, status_code=500)

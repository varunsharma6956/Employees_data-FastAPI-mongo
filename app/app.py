from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.router.get_employee_router import get_employee_router
from app.router.post_employee_router import post_employee_router
from app.router.update_employee_router import update_employee_router
from app.router.delete_employee_router import delete_employee_router
from app.router.put_employee_router import put_employee_router

def create_app():
    app = FastAPI()

    # Configure CORS
    origins = ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include router
    app.include_router(get_employee_router)
    app.include_router(post_employee_router)
    app.include_router(update_employee_router)
    app.include_router(delete_employee_router)
    app.include_router(put_employee_router)

    return app

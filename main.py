import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from app.app import create_app

app = create_app()

# Configure CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

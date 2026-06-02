from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from predict import router as predict_router
from chatbot import router as chatbot_router

app = FastAPI(
    title="Heart Disease Detection API",
    version="1.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routes
app.include_router(predict_router)
app.include_router(chatbot_router)

@app.get("/")
def home():
    return {
        "message": "Heart Disease Detection API Running Successfully"
    }
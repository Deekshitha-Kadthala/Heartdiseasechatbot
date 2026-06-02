from fastapi import APIRouter, UploadFile, File
import random

router = APIRouter()

@router.post("/predict")
async def predict(file: UploadFile = File(...)):

    # Random prediction
    predictions = [
        "Heart Disease Detected",
        "No Heart Disease Detected"
    ]

    prediction = random.choice(predictions)

    confidence = random.randint(10, 99)

    # Different messages
    if prediction == "Heart Disease Detected":

        message = (
            "Possible heart-related abnormalities found."
        )

    else:

        message = (
            "Heart appears normal and healthy."
        )

    return {
        "prediction": prediction,
        "confidence": confidence,
        "message": message
    }
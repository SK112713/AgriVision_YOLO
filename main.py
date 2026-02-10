from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
from ultralytics import YOLO
from PIL import Image
import io
import cv2
import numpy as np
import uvicorn

app = FastAPI()

# 1. Load your custom trained model
# Ensure 'best.pt' is in the same folder
try:
    model = YOLO("best.pt")
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")

@app.get("/")
def home():
    return {"message": "Plant Disease Detection API is running!"}

@app.post("/detect")
async def detect_disease(file: UploadFile = File(...)):
    # 2. Read the uploaded image
    try:
        image_data = await file.read()
        image = Image.open(io.BytesIO(image_data))
    except Exception as e:
        return {"error": f"Invalid image file: {e}"}

    # 3. Run prediction using standard YOLO
    # conf=0.25 filters out weak predictions
    results = model.predict(image, conf=0.25)

    # 4. Generate the image with bounding boxes
    # plot() returns a NumPy array (BGR format) suitable for OpenCV
    result_image_bgr = results[0].plot()
    
    # 5. Convert the NumPy array to a valid image format (JPEG)
    success, encoded_image = cv2.imencode('.jpg', result_image_bgr)
    
    if not success:
        return {"error": "Could not process image"}

    # 6. Return the image bytes directly
    return Response(content=encoded_image.tobytes(), media_type="image/jpeg")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
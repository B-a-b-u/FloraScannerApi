from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import tensorflow as tf
from io import BytesIO
from PIL import Image
import numpy as np
import requests
from plant_medicinal_data import Plant_Details, class_list


app = FastAPI()

# Allow all origins to access the API (replace '*' with your frontend URL in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Load the model
model = tf.keras.models.load_model("models/model-3.keras")

# Define class labels (replace this with your actual class labels)


# Helper function to get plant name
def get_plant_name(plant_name):
    return Plant_Details.get(plant_name)[0]

# Endpoint to predict image
@app.post("/predict-image")
async def predict_image(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = np.array(Image.open(BytesIO(contents)))
        prediction = model.predict(np.expand_dims(image,0))
        predicted_class_index = np.argmax(prediction)
        confidence = round(100 * np.max(prediction[0]), 2)
        predicted_class = class_list[predicted_class_index]
        plant_details = get_plant_name(predicted_class)
        return {
            "class": predicted_class,
            "confidence": confidence,
            "details": plant_details
        }
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

# Endpoint to predict image from URL
@app.post("/predict-url")
async def predict_url(image_url: str):
    try:
        # Download the image from the URL
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
        image = np.array(image)

        # Predict the image
        prediction = model.predict(np.expand_dims(image, 0))
        predicted_class_index = np.argmax(prediction)
        confidence = round(100 * np.max(prediction[0]), 2)
        predicted_class = class_list[predicted_class_index]
        plant_details = get_plant_name(predicted_class)
        return {
            "class": predicted_class,
            "confidence": confidence,
            "details": plant_details
        }
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

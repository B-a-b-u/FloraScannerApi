from fastapi import FastAPI, Body, HTTPException, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import tensorflow as tf
from io import BytesIO
from PIL import Image
import numpy as np
from plant_medicinal_data import Plant_Details, class_list
import base64


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
model = tf.keras.models.load_model("models/newmodel1.keras")

# Define class labels (replace this with your actual class labels)


# Helper function to get plant name
def get_plant_name(plant_name):
    return Plant_Details.get(plant_name)

@app.get("/")
async def home():
    return {"message": "Welcome to the Flora Scanner API!"}

@app.post("/predict")
async def predict_image(image_data: dict = Body(...)):
    try:
        # Decode base64 image data
        image_base64 = image_data.get("image")
        if not image_base64:
            raise HTTPException(status_code=400, detail="Image data not provided")
        image_bytes = base64.b64decode(image_base64)
        image = np.array(Image.open(BytesIO(image_bytes)))
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
# @app.post("/predict-url")
# async def predict_url(image_url: str):
#     try:
#         # Download the image from the URL
#         response = requests.get(image_url)
#         image = Image.open(BytesIO(response.content))
#         image = np.array(image)

#         # Predict the image
#         prediction = model.predict(np.expand_dims(image, 0))
#         predicted_class_index = np.argmax(prediction)
#         confidence = round(100 * np.max(prediction[0]), 2)
#         predicted_class = class_list[predicted_class_index]
#         plant_details = get_plant_name(predicted_class)
#         return {
#             "class": predicted_class,
#             "confidence": confidence,
#             "details": plant_details
#         }
#     except Exception as e:
#         return JSONResponse(content={"error": str(e)}, status_code=500)

@app.post("/predicttest")
async def predict_image(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = np.array(Image.open(BytesIO(contents)))
        image = np.array(Image.open(BytesIO(image)))
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

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

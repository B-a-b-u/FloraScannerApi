from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from plant_medicinal_data import Plant_Details, class_list
import tensorflow as tf
from io import BytesIO
from PIL import Image
import numpy as np
import uvicorn


model = tf.keras.models.load_model("models/model-3.keras")
app = FastAPI()

@app.get("/")
async def home():
    return {"message" : "Hello World"}


def get_plant_name(plant_name):
    return Plant_Details.get(plant_name)[0]

@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = np.array(Image.open(BytesIO(contents)))
        # print(model)
        prediction = model.predict(np.expand_dims(image,0))
        predicted_class_index = np.argmax(prediction)
        conf = round(100 * (np.max(prediction[0])),2)
        predicted_class = class_list[predicted_class_index]
        return JSONResponse(content={"class": predicted_class,"confidence" : conf, "details ":get_plant_name(predicted_class)}, status_code=200)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port = 8000)

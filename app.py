import os
import sys

import uvicorn
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import Response
from starlette.responses import RedirectResponse
from pydantic import BaseModel

from src.pipeline.predict_pipeline import PredictPipeline


class TextRequest(BaseModel):
    text: str

app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def training():
    try:
        os.system("python src/pipeline/train_pipeline.py")
        return Response("Training completed successfully!")
    except Exception as e:
        return Response(f"Error occurred during training: {e}")
    
@app.post("/predict")
async def predict_route(request: TextRequest):
    try: 
        obj = PredictPipeline()
        result = obj.predict(request.text)
        return {"summary": result}
    except Exception as e:
        raise e
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

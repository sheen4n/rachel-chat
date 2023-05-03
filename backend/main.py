from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai

# Custom Function Imports
# ...

# Initiate App
app = FastAPI()

# CORS - Origin


@app.get("/")
async def root():
    return {"message": "Hello World"}

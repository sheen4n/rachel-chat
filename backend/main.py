from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai

# Custom Function Imports
from functions.openai_requests import convert_audio_to_text

# Initiate App
app = FastAPI()

# CORS - Origins
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:4174",
    "http://localhost:3000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/health")
async def check_health():
    return {"message": "Healthy"}


@app.get("/post-audio-get/")
async def get_audio():

    # Get saved audio
    audio_input = open("voice.mp3", "rb")

    # Decode audio
    message_decoded = convert_audio_to_text(audio_input)

    print(message_decoded)

    return "Done"
# Post bot response
# Note: Not playing in browser when using post request
# @app.post("/post-audio/")
# async def post_audio(file: UploadFile = File(...)):
#     print("hello")


# Run app with main:app --reload for development
# access docs with http://localhost:8000/docs

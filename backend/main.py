from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai


# Custom Function Imports
from functions.openai_requests import convert_audio_to_text, get_chat_response
from functions.database import store_messages, reset_messages
from functions.text_to_speech import convert_text_to_speech

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


@app.get("/reset")
async def reset_conversation():
    reset_messages()
    return {"message": "conversation reset"}


@app.post("/post-audio/")
async def post_audio(file: UploadFile = File(...)):
    print("api post audio get trigger")

    # # Get saved audio
    # audio_input = open("voice.mp3", "rb")

    # Save File From Frontend
    with open(file.filename, "wb") as buffer:
        buffer.write(file.file.read())
    audio_input = open(file.filename, "rb")

    # Decode audio
    message_decoded = convert_audio_to_text(audio_input)

    # Guard: Ensure message decoded
    if not message_decoded:
        return HTTPException(status_code=400, detail="Failed to decode audio")

    # Get ChatGPT Response

    chat_response = get_chat_response(message_decoded)

    # Guard: If no chat response
    if not chat_response:
        return HTTPException(status_code=400, detail="Failed to get chat response")

    # Convert chat response to audio
    audio_output = convert_text_to_speech(chat_response)

    # Store message
    store_messages(message_decoded, chat_response)
    # print(chat_response)

    if not audio_output:
        return HTTPException(status_code=400, detail="Failed to get audio response from eleven labs")

    # Create a generator that yields chunks of data

    def iterfile():
        yield audio_output

    # Return audio file
    return StreamingResponse(iterfile(), media_type="application/octet-stream")


# Post bot response
# Note: Not playing in browser when using post request
# @app.post("/post-audio/")
# async def post_audio(file: UploadFile = File(...)):
#     print("hello")


# Run app with main:app --reload for development
# access docs with http://localhost:8000/docs

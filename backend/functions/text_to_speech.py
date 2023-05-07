import requests

from decouple import config

ELEVEN_LABS_API_KEY = config("ELEVEN_LABS_API_KEY")
ELEVEN_LABS_VOICE_ID = config("ELEVEN_LABS_VOICE_ID")


# Eleven Labs
# Convert Text to Speech

def convert_text_to_speech(message):

    # Define Request Body
    body = {
        "text": message,
        "voice_settings": {
            "stability": 0,
            "similarity_boost": 0
        }
    }

    # Define headers
    headers = {"xi-api-key": ELEVEN_LABS_API_KEY,
               "Content-Type": "application/json",
               "accept": "audio/mpeg"}

    # Define endpont
    endpoint = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVEN_LABS_VOICE_ID}"

    # Send request

    try:
        response = requests.post(endpoint, json=body, headers=headers)
    except Exception as e:
        print("convert_text_to_speech", e)
        return

    # Handle response
    if response.status_code == 200:
        return response.content

    return

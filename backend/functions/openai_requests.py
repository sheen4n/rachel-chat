import openai
from decouple import config

from functions.database import get_recent_messages

# Retrieve Environment Varaibles
openai.organization = config("OPEN_AI_ORG")
openai.api_key = config("OPEN_AI_KEY")

# Open AI - Whisper
# Convert Audio To Text


def convert_audio_to_text(audio_file):
    try:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        message_text = transcript["text"]
        return message_text
    except Exception as e:
        print("convert_audio_to_text", e)
        return

# Open AI - ChatGPT
# Get Response to our Message


def get_chat_response(message_input):
    messages = get_recent_messages()
    user_message = {"role": "user", "content": message_input}
    messages.append(user_message)
    print("get_chat_response_messages", messages)

    try:
        print("calling openai api...")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages)

        # print(response)
        message_text = response["choices"][0]["message"]["content"]
        return message_text
    except Exception as e:
        print("get_chat_response", e)
        return

import json
import random

# Get recent messages


def get_recent_messages():
    # Define the file name and learn instructions
    file_name = "stored_data.json"
    learn_instructions = {
        "role": "system",
        "content": "You are interviewing the user for a job as a retail assistant. Ask short questions that relevant to the junior position. Your name is Rachel. The user is called Shaun. Keep your answers to under 30 words."
    }

    # Initialize messages
    messages = []

    # Add a random element
    x = random.uniform(0, 1)
    if x < 0.5:
        learn_instructions["content"] += " Your response will include some dry humour."
    else:
        learn_instructions["content"] += "Your response will include a rather challenging question."

    # Append instruction to message
    messages.append(learn_instructions)

    # Get last messages
    try:
        with open(file_name) as user_file:
            data = json.load(user_file)

            # Append last 5 items of data
            if data:
                messages += data[-5]
    except Exception as e:
        print(e)

    # Return
    return messages

# Store Messages


def store_messages():
    pass

import json
import random

# Get recent messages

# DB_FILE
DB_FILE = "stored_data.json"


def get_recent_messages():
    # Define the file name and learn instructions
    file_name = DB_FILE
    learn_instructions = {
        "role": "system",
        "content": "You are interviewing the user for a job as a retail assistant. Ask short questions that relevant to the junior position. Your name is Rachel. The user is called Charlie. Keep your answers to under 30 words."
    }

    # Initialize messages
    messages = []

    # Add a random element
    x = random.uniform(0, 1)
    if x < 0.5:
        learn_instructions["content"] += " Your response will include some light hearted humour."
    else:
        learn_instructions["content"] += "Your will have a playful tone."

    # Append instruction to message
    messages.append(learn_instructions)

    # Get last messages
    try:
        with open(file_name) as user_file:
            data = json.load(user_file)

            # Append last 5 items of data
            if data:
                messages += data[-5:]
    except Exception as e:
        print("database", e)

    # Return
    return messages

# Store Messages


def store_messages(request_message, response_message):
    # Define the file name
    file_name = DB_FILE

    # Get recent messages
    messages = get_recent_messages()[1:]

    # Add messages to data
    user_message = {"role": "user", "content": request_message}
    assistant_message = {"role": "assistant", "content": response_message}

    messages.append(user_message)
    messages.append(assistant_message)

    # Save the updated file
    with open(file_name, "w") as f:
        json.dump(messages, f)


# Reset Messages
def reset_messages():
    # Over current file with nothing
    open(DB_FILE, "w")

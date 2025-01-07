import os
import json
import utils
import time

import openai
from openai import OpenAI
client = OpenAI()

gpt_model = "gpt-3.5-turbo-1106"

def chat_completions_request(messages, model=gpt_model, json_mode=True):
    api_params = {
        "model": model,
        "messages": messages,
        "temperature": 0
    }
    
    if json_mode:
        api_params["response_format"] = { "type": "json_object" } 
    
    response = client.chat.completions.create(**api_params)
    return response.choices[0].message

def process_transcript(transcript):
    pass

if __name__ == "__main__":
    directory_path = "transcripts"
    files = os.listdir(directory_path)

    for file in files:
        if file.endswith('.txt'):
            file_path = os.path.join(directory_path, file)

            process_transcript(utils.open_file(file_path))


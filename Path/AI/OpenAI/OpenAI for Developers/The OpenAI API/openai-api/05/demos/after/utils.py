import os
from termcolor import colored
from datetime import datetime, timedelta
import json
import textwrap
import re
import tiktoken
from openai.types.chat import ChatCompletionMessage

def pretty_print_conversation(messages):
    """
    Prints the conversation with messages color-coded based on the role of the sender.

    The function accepts a list of dictionaries, where each dictionary represents a message.
    Each message dictionary should contain a 'role' key indicating the sender's role 
    (i.e., 'system', 'user', 'assistant', 'tool') and a 'content' key indicating the 
    message's content. For 'assistant' messages, they could optionally include a 'tool' key.
    For 'function' messages, they should include a 'name' key indicating the function's name.
    
    Each message is printed on a new line with a color associated with the role of the sender: 
    'system' messages are magenta, 'user' messages are green, 'assistant' messages are yellow, 
    and 'tool/function' messages are blue.

    Parameters
    ----------
    messages : list
        A list of dictionaries where each dictionary represents a message in the conversation.
        Each dictionary must contain 'role' and 'content' keys. 'assistant' messages could 
        optionally include a 'tool' key, and 'function' messages should include a 'name' key.

    """
    role_to_color = {
        "system": "magenta",
        "user": "green",
        "assistant": "yellow",
        "tool": "blue",
    }
    for raw_message in messages:
        message = raw_message
        if isinstance(raw_message, ChatCompletionMessage):
            message = raw_message.dict()
        
        if message["role"] == "system":
            print(colored(f"system: {message['content']}\n", role_to_color[message["role"]]))
        elif message["role"] == "user":
            print(colored(f"user: {message['content']}\n", role_to_color[message["role"]]))
        elif message["role"] == "assistant" and message.get("tool_calls"):
            print(colored(f"assistant: {message['tool_calls']}\n", role_to_color[message["role"]]))
        elif message["role"] == "assistant" and not message.get("tool_calls"):
            print(colored(f"assistant: {message['content']}\n", role_to_color[message["role"]]))
        elif message["role"] == "tool":
            print(colored(f"function ({message['name']}): {message['content']}\n", role_to_color[message["role"]]))

def open_file(file_name):
    """
    Open a file and return its content.

    Parameters
    ----------
    file_name : str
        The name (including path) of the file to open.

    Returns
    -------
    str
        The content of the file.
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()

def save_file(content, file_name):
    """
    Save the provided content into a file with the given name. 
    If the directory of the file doesn't exist, it will be created.

    Parameters
    ----------
    content : str
        The content to be written to the file.
    file_name : str
        The name (including path) of the file to write the content to.
    """
    directory = os.path.dirname(file_name)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(content)

def get_scheduled_date(date):
    """
    Add seven days to the provided date and return the new date.

    Parameters
    ----------
    date : str
        The input date as a string in the format of "%Y-%m-%dT%H:%M:%SZ" 
        (e.g., "2023-07-10T12:00:00Z").

    Returns
    -------
    str
        The new date as a string in the same format as the input date,
        seven days later.
    """
    # Format of the input date
    date_format = "%Y-%m-%dT%H:%M:%SZ"
    
    # Convert the string to a datetime object
    date_object = datetime.strptime(date, date_format)

    # Add seven days to the date
    new_date = date_object + timedelta(days=7)

    # Convert the new date back to a string
    return new_date.strftime(date_format)

def schedule_follow_up(interviewer, candidate, interview_date, sentiment=None):
    """
    Schedule a follow-up interview.

    Parameters
    ----------
    interviewer : str
        The name of the interviewer.
    candidate : str
        The name of the candidate.
    interview_date : str
        The date of the first interview.
    sentiment : str, optional
        The sentiment after the initial interview.

    Returns
    -------
    str
        A JSON string containing the details of the follow-up interview.
    """
    new_date_str = get_scheduled_date(interview_date)  # Get the formatted date string.

    response = {
        "interviewer": interviewer,  # Interviewer's name.
        "candidate": candidate,  # Candidate's name.
        "scheduled_date": new_date_str  # Formatted date string.
    }
    if sentiment is not None:
        response["sentiment"] = sentiment  # Sentiment after the initial interview.

    return json.dumps(response)  # Convert the response dictionary to a JSON string.

def get_follow_up_function_desc():
    """
    Constructs and returns a list of dictionaries containing the JSON schema for the schedule_follow_up function.
    
    Returns:
        list: A list of dictionaries containing details about the schedule_follow_up function. 
              Each dictionary contains the name, description and parameters required by the function.
    """
    # Define a dictionary that serves as the JSON schema for the function schedule_follow_up
    return [
        {
            "type": "function",
            "function": {
                "name": "schedule_follow_up",  # Name of the function
                "description": "Get the details of the scheduled follow-up call",  # Description of the function
                "parameters": {
                    "type": "object",  # Type of parameters to be supplied
                    "properties": {  # Parameter details
                        "interviewer": {
                            "type": "string",  # Type of the 'interviewer' parameter
                            "description": "Name of the interviewer"  # Description of the 'interviewer' parameter
                        },
                        "candidate": {
                            "type": "string",  # Type of the 'candidate' parameter
                            "description": "Name of the candidate"  # Description of the 'candidate' parameter
                        },
                        "interview_date": {
                            "type": "string",  # Type of the 'interview_date' parameter
                            "format": "date-time",  # Expected format of the 'interview_date' parameter
                            "description": "The date and time of the interview in ISO 8601 format"  # Description of the 'interview_date' parameter
                        },
                        "sentiment": {
                            "type": "string",  # Type of the 'sentiment' parameter
                            "enum": ["positive", "negative", "neutral"],  # Accepted values for the 'sentiment' parameter
                            "description": "The sentiment of the interview."  # Description of the 'sentiment' parameter
                        }
                    },
                    "required": ["interviewer", "candidate", "interview_date"]  # Required parameters for the function
                }
            }
        }
    ]

def split_text_simple(text, length_limit=2000):
    """
    Splits a given text into chunks each with maximum length as length_limit.
    This function splits text without considering paragraph structure.

    Parameters
    ----------
    text : str
        The text to split.
    length_limit : int, optional
        The maximum character length of each chunk (default is 2000).

    Returns
    -------
    list of str
        The list of split chunks.
    """
    return textwrap.wrap(text, length_limit)

def split_text_advanced(text, length_limit=2000):
    """
    Splits a given text into chunks each with maximum length as length_limit.
    This function splits text considering paragraph structure.

    Parameters
    ----------
    text : str
        The text to split.
    length_limit : int, optional
        The maximum character length of each chunk (default is 2000).

    Returns
    -------
    list of str
        The list of split chunks respecting paragraph boundaries.
    """
    # Split text into paragraphs using single or double line breaks
    paragraphs = re.split(r'\n\n|\n(?!\n)', text)
    lines = []

    for paragraph in paragraphs:
        # Split each paragraph into lines with maximum length as length_limit
        lines.extend(textwrap.wrap(paragraph, length_limit))

    return lines

def format_moderation_response(response, text):
    """
    Formats and prints the moderation response from OpenAI's API.

    This function takes the response from the moderation API and the text that was checked.
    It prints whether the text violates the content policy, the model used for the check,
    the categories that were evaluated, and the corresponding scores for each category.

    It does not return any value.

    Parameters
    ----------
    response : object
        The response object returned from OpenAI's moderation API.
                         This should contain the results of the content moderation check,
                         including categories and category scores.
    text : str
        The text that was submitted for moderation.
    """

    # Extracting categories and category scores from the response
    categories = response.results[0].categories
    category_scores = response.results[0].category_scores

    # Informing if the text violates the content policy
    print(f"Text violates content policy: \n{text}\n")
    
    # Printing the model used for moderation
    print(f"Moderation model: {response.model}\n")

    # Iterating over the categories to print them
    print("Categories:")
    for category, value in categories.__dict__.items():
        # Formatting category names and printing their values
        print(f"  {category.replace('_', ' ').capitalize()}: {value}")

    # Iterating over the category scores to print them
    print("\nCategory Scores:")
    for category, score in category_scores.__dict__.items():
        # Formatting category names and printing their scores
        print(f"  {category.replace('_', ' ').capitalize()}: {score:.2f}")

def num_tokens_from_messages(messages, model="gpt-3.5-turbo-0613"):
    """Return the number of tokens used by a list of messages."""
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        print("Warning: model not found. Using cl100k_base encoding.")
        encoding = tiktoken.get_encoding("cl100k_base")
    if model in {
        "gpt-3.5-turbo-0613",
        "gpt-3.5-turbo-16k-0613",
        "gpt-4-0314",
        "gpt-4-32k-0314",
        "gpt-4-0613",
        "gpt-4-32k-0613",
        }:
        tokens_per_message = 3
        tokens_per_name = 1
    elif model == "gpt-3.5-turbo-0301":
        tokens_per_message = 4  # every message follows <|start|>{role/name}\n{content}<|end|>\n
        tokens_per_name = -1  # if there's a name, the role is omitted
    elif "gpt-3.5-turbo" in model:
        print("Warning: gpt-3.5-turbo may update over time. Returning num tokens assuming gpt-3.5-turbo-0613.")
        return num_tokens_from_messages(messages, model="gpt-3.5-turbo-0613")
    elif "gpt-4" in model:
        print("Warning: gpt-4 may update over time. Returning num tokens assuming gpt-4-0613.")
        return num_tokens_from_messages(messages, model="gpt-4-0613")
    else:
        raise NotImplementedError(
            f"""num_tokens_from_messages() is not implemented for model {model}. See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens."""
        )
    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        message_dict = message
        if isinstance(message, ChatCompletionMessage):
            message_dict = message.model_dump()
        for key, value in message_dict.items():
            num_tokens += len(encoding.encode(get_safe_string(value)))
            if key == "name":
                num_tokens += tokens_per_name

    num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
    return num_tokens

def get_safe_string(value):
    """
    Converts the input value to a string in a safe manner. 

    Parameters
    ----------
    value : str
        The value to be converted to string.

    Returns
    ----------
    A string representation of the input value.
    """

    if value is None:  # If the value is None
        return ''  # Return an empty string
    elif isinstance(value, str):  # If the value is already a string
        return value  # Return the value as is
    elif isinstance(value, dict) or isinstance(value, list):  # If the value is a JSON object or array
        return json.dumps(value)  # Convert JSON object/array to string and return
    else:  # For all other data types
        return str(value)  # Convert the value to string and return

def print_token_info(messages, model, response, price_per_input_token, price_per_output_token):
    """
    Prints the token count and cost information for the given messages and response.

    Parameters
    ----------
    messages:
        The messages for which the token count is to be calculated.
    model:
        The model used to calculate the token count.
    response:
        The response received from the OpenAI API, which includes the usage data.
    price_per_input_token:
        The cost per input token.
    price_per_output_token:
        The cost per output token.
    """

    # Calculate the number of tokens from the messages
    tokens = num_tokens_from_messages(messages, model)
    # Calculate the cost for the input tokens
    cost = price_per_input_token * tokens
    # Print the token count and cost
    print(f"{tokens} prompt tokens counted by tiktoken. Cost: ${cost}")

    # Get the number of prompt tokens from the response
    prompt_tokens = response.usage.prompt_tokens
    # Calculate the cost for the prompt tokens
    cost = price_per_input_token * prompt_tokens
    # Print the token count and cost
    print(f'{prompt_tokens} prompt tokens counted by the OpenAI API. Cost: ${cost}') 

    # Get the number of completion tokens from the response
    completion_tokens = response.usage.completion_tokens
    # Calculate the cost for the completion tokens
    cost = price_per_output_token * completion_tokens
    # Print the token count and cost
    print(f'{completion_tokens} completion tokens counted by the OpenAI API. Cost: ${cost}')

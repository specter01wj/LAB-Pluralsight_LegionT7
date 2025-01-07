import os
from termcolor import colored
from datetime import datetime, timedelta
import json
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
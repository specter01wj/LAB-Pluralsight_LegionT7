import os
from openai import OpenAI

# Set the API key with the environment variable OPENAI_API_KEY
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Ask the user for their question
user_question = input("Please enter you question about C# programming: ")

# Call the API passing the list of messages
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a C# programmer with years of experience. I'll ask questions about C# programming, best practices, troubleshooting, or any related topics, and you'll answer in a helpful and friendly way with a code snippet and/or a brief explanation."},
    {"role": "user", "content": user_question}
  ],
  temperature=0
)

# Print the response message object
print(completion.choices[0].message)

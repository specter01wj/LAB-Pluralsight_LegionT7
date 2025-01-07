import os
from openai import OpenAI
import base64

# Set the API key with the environment variable OPENAI_API_KEY
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Make the API request
response = client.images.generate(
  model="dall-e-3",
  prompt="A cute white cat",
  n=1,
  size="1024x1024",
  response_format="b64_json"
)

#print(response)

# Iterate through the data in the response
for i, image in enumerate(response.data):
    # The image data is base64 encoded, so decode it
    image_data = base64.b64decode(image.b64_json)
    
    # Save the image data to a file
    with open(f'image_{i}.png', 'wb') as f:
        f.write(image_data)
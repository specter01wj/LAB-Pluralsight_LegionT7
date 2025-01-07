import os
from openai import OpenAI

# Set the API key with the environment variable OPENAI_API_KEY
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Open the audio file, change the name if necessary
audio_file = open("audio.wav", "rb")

# Call the audio API to transcribe the audio
transcript = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)

# Print the API response
print(transcript)

# Open the audio file again, change the name if necessary
audio_file = open("audio.wav", "rb")

# Call the audio API to transcribe the audio using a prompt to improve the quality
transcript = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file,
  prompt="Welcome to AI for Beginners! We'll be exploring super cool AI (Artificial Intelligence) concepts. Particularly, RNNs (Recurrent Neural Networks). So, let's jump right in."
)

# Print the API response
print(transcript)
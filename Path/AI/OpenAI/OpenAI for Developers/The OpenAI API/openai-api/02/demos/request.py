import http.client
import json
import os

conn = http.client.HTTPSConnection("api.openai.com")

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer OPENAI_API_KEY'
}

payload = json.dumps({
  "model": "gpt-3.5-turbo",
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant."
    },
    {
      "role": "user",
      "content": "Dog in Italian is:"
    }
  ]
})

conn.request("POST", "/v1/chat/completions", body=payload, headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
function ChatAPI(cellText) {
  const url = "https://api.openai.com/v1/chat/completions";
  const parameters = {
    method: "POST",
    contentType: "application/json",
    headers: {
      "Authorization": "Bearer " + "OPENAI_API_KEY",
    },
    payload: JSON.stringify({
      "model": "gpt-3.5-turbo",
      "messages": [
        {
          "role": "system",
          "content": "You are a helpful assistant."
        },
        {
          "role": "user",
          "content": cellText + " in Italian is:"
        }
      ]
    }),
  };
  
  const response = UrlFetchApp.fetch(url, parameters);
  const data = JSON.parse(response.getContentText());
  const message = data.choices[0].message.content; // Accessing the response content

  return message;
}
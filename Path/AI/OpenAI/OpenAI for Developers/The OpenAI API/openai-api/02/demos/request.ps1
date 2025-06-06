# PowerShell script to execute a curl request using curl.exe

# Your OpenAI API key
$OPENAI_API_KEY = "YOUR_OPENAI_KEY"

# Execute the curl request using curl.exe
& curl.exe "https://api.openai.com/v1/chat/completions" `
  -H "Content-Type: application/json" `
  -H "Authorization: Bearer $($OPENAI_API_KEY)" `
  -d '{
    \"model\": \"gpt-3.5-turbo\",
    \"messages\": [
      {
        \"role\": \"system\",
        \"content\": \"You are a helpful assistant.\"
      },
      {
        \"role\": \"user\",
        \"content\": \"Dog in Italian is:\"
      }
    ]
  }'

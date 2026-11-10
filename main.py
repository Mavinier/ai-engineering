import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from datetime import datetime

# Load environment variables from .env
load_dotenv()

# Validate API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY not found in environment variables")

# Initialize Gemini client
client = genai.Client(
    api_key=api_key,
    http_options=types.HttpOptions(timeout=120000)
)

print("Sending request...", datetime.now(), flush=True)

# Send request to the model
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="Reply with exactly: OK",
    config=types.GenerateContentConfig(
        max_output_tokens=20
    )
)

print("Answer received", datetime.now(), flush=True)

# Display response
print(response.text)
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Centralized configurations
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not OPENAI_API_KEY and not GEMINI_API_KEY:
    print("[WARNING]: No API key found. Set OPENAI_API_KEY or GEMINI_API_KEY in your .env file.")
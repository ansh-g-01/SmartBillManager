import os
import pytesseract
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# OCR config
pytesseract.pytesseract.tesseract_cmd = os.getenv("TESSERACT_CMD")

# Set environment variables
groq_api_key = os.getenv("GROQ_API_KEY")
# Email config
EMAIL = os.getenv("EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")

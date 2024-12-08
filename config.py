import os

from dotenv import load_dotenv

load_dotenv()

HOST = os.environ.get("HOST", "127.0.0.1")
PORT = int(os.environ.get("PORT", 5000))
DEBUG = os.environ.get("DEBUG", "true") == "true"

API_KEY = os.environ.get("API_KEY")
BASE_URL = os.environ.get("BASE_URL", "http://dataservice.accuweather.com")

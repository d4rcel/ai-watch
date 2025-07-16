import os
from dotenv import load_dotenv


load_dotenv()

GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
GOOGLE_SHEET_NAME = os.getenv("GOOGLE_SHEET_NAME")
SPREDSHEED_KEY = os.getenv("SPREDSHEED_KEY")
RSS_FEEDS = os.getenv("RSS_FEEDS", "").split(",")
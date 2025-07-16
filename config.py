from os import environ as env, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


class Config:
    """Set Flask configuration from .env file."""

    # General Config
    GOOGLE_APPLICATION_CREDENTIALS = env.get("GOOGLE_APPLICATION_CREDENTIALS")
    GOOGLE_SHEET_NAME = env.get("GOOGLE_SHEET_NAME")
    SPREADSHEET_KEY = env.get("SPREADSHEET_KEY")

    RSS_FEEDS = env.get("RSS_FEEDS", "").split(',')
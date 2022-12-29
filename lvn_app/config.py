import os

class Config(object):
    MODE = os.environ.get('MODE')
    PIANO_APP_ID = os.environ.get('PIANO_APP_ID')
    PIANO_API_TOKEN = os.environ.get("PIANO_API_TOKEN")
    PIANO_PRIVATE_KEY = os.environ.get("PIANO_PRIVATE_KEY")
    MVAULT_USERNAME = os.environ.get("MVAULT_USERNAME")
    MVAULT_PASSWORD = os.environ.get("MVAULT_PASSWORD")
    MVAULT_STATION_ID = os.environ.get("MVAULT_STATION_ID")
    MVAULT_KEY = os.environ.get("MVAULT_KEY")
    MVAULT_SECRET = os.environ.get("MVAULT_SECRET")
    MVAULT_API = os.environ.get("MVAULT_API")
    MVAULT_PASSPORT_MEMBERSHIP = os.environ.get("MVAULT_PASSPORT_MEMBERSHIP")
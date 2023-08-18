import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

class Settings:
    URL = "https://docs.google.com/spreadsheets/d/1EBLY6bUDjbt81vDljIoxfvaQiarXr6LVn3Iyvw0eiHk/edit?usp=sharing"
    SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
    ]
    SECRET_FILE = "secrets.json"
    
    
class MyClient:
    def __init__(self, url, scopes, secret_file):
        creds = ServiceAccountCredentials.from_json_keyfile_name(secret_file, scopes=scopes)
        self.client = gspread.authorize(credentials=creds)
        self.data = self.client.open_by_url(url)

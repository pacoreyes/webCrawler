# -----------------------------------------------------------
# initialization of database instances
# Firebase, Google Drive, SQLite
#
# (C) 2021-2024 Juan-Francisco Reyes, Cottbus, Germany
# Brandenburg University of Technology, Germany.
# Released under MIT License
# email pacoreyes.zwei@gmail.com
# -----------------------------------------------------------
import gspread
from utils import load_json_file
from oauth2client.service_account import ServiceAccountCredentials
import firebase_admin
from firebase_admin import credentials, firestore

# Use the service account credentials to initialize the app
cred = credentials.Certificate('credentials/firebase_credentials.json')
firebase_admin.initialize_app(cred)

# Get the Firestore client
firestore_db = firestore.client()

""" Initialize Google Sheets """
gdrive_scope = ["https://www.googleapis.com/auth/spreadsheets",
                "https://www.googleapis.com/auth/drive"]
sheet_id = load_json_file("credentials/gsheets_credentials.json")["sheet_id"]
cred = ServiceAccountCredentials.from_json_keyfile_name("credentials/gsheets_credentials.json", gdrive_scope)
client = gspread.authorize(cred)
spreadsheet = client.open_by_key(sheet_id)  # Initialize the spreadsheet

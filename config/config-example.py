import firebase_admin
from firebase_admin import credentials

config = {
  "apiKey": "xxxxxxxxxxxxxxxxxxxx",
  "authDomain": "xxxxxxxx.firebaseapp.com",
  "databaseURL": "https://xxxxxxxxx.firebaseio.com",
  "projectId": "xxxxxxxxxxxx",
  "storageBucket": "xxxxxxxxxxxx.appspot.com",
  "messagingSenderId": "xxxxxxxxxxxxxx"
}

cred = credentials.Certificate('./config/ServiceAccountKey.json')
firebase_admin.initialize_app(cred)
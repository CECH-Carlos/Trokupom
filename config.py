DEBUG = True

HOST = "0.0.0.0"

PORT = "3000"

config = {
  "apiKey": "AIzaSyCo0WR0_b6dByreBhZHiOpE9smw1YFTgho",
  "authDomain": "skambo-app.firebaseapp.com",
  "projectId": "skambo-app",
  "storageBucket": "skambo-app.appspot.com",
  "messagingSenderId": "195234467935",
  "appId": "1:195234467935:web:825a3cf2be8565113f8bea",
  "measurementId": "G-XD32LDS4LW",
  "databaseURL": "https://console.firebase.google.com/u/2/project/skambo-app/firestore/data/~2F"
}

firebaseConfig = config

admin_list = {
    'carlos.decastrohenriques@gmail.com',
    'Ianmakdi@gmail.com',
    'leonardodaredevil@gmail.com',
    'dansmonvieuxcartable@gmail.com',
    'batatas.churros@gmail.com'
}

path_on_cloud = "uploads-dos-usuarios/ideapad.jpg"
path_local = ""

#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:fasYqCpVGgmzyAciJlsEMuR@35.198.61.92/skambo-app'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Carlos.....c3!@localhost/trokupom'
SQLALCHEMY_TRACK_MODIFICATIONS = True

UPLOAD_FOLDER = 'static/uploads/'

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

MAX_CONTENT_LENGTH = 16 * 1024 * 1024

'''
    Secret key creation logic:
    
    |A|tila
    |c|arlos
    |I|an
    |j|air
    |L|eonardo
    |s|ilva
    |E|duardo
    |m|akdisse
    |U|rbano
    |r|ocha

    |A c I j L s E m U r|
'''

SECRET_KEY = 'AcIjLsEmUr'
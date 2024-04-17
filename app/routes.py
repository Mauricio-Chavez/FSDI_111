from flask import Flask

app = Flask(__name__)

@app.get('/')
def index():
    me = {
        "first_name": "Mauricio",
        "last_name": "Chavez" ,
        "hobbies": "VideoGames",
        "is_online": True
    }
    return me
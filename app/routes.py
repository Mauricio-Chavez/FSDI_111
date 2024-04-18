from flask import Flask

app = Flask(__name__)

@app.get('/')
@app.get('/about')
def aboutMe():
    me = {
        "first_name": "Mauricio",
        "last_name": "Chavez" ,
        "hobbies": "VideoGames",
        "is_online": True
    }
    return me
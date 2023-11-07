from flask import Flask, render_template
from flask_cors import CORS


app = Flask(__name__,template_folder="./template")
cors = CORS(app)


# inputPath recommand : "/usr/src/LeArNER/input/{}.txt"

@app.route('/')
def homePage():
    return render_template('homepage.html')



from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__,template_folder="./template")
cors = CORS(app)

@app.route('/')
def homePage():
    return render_template('homepage.html')

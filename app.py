from flask import Flask, request, session
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

lm = LoginManager() 
lm.init_app(app)



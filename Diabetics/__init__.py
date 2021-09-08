from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY']='b4491168f49f7b962953f8a6a3eaa6e7'

from Diabetics import router
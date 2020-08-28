from flask import Flask
from flask import request, render_template

from config import BaseConfig
flask_app = Flask(__name__)
flask_app.config.from_object(BaseConfig)
@flask_app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

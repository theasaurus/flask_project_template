from flask import Flask
from app.db import init_app
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
init_app(app)

from app import routes

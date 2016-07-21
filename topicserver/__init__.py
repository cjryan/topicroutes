"""
The flask application package.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('topicserver.config')
db = SQLAlchemy(app)

from topicserver import views, models

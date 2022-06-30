from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from config.postgresl import *
from config.flask_config import app

# initializing sqlalchemy
db = SQLAlchemy(app)


# creating of the model
class Note(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    text = db.Column(db.String(100))
    complete = db.Column(db.Boolean())
    date = db.Column(db.DateTime(timezone=True), default=func.now())


# for creating a table in database.
db.create_all()
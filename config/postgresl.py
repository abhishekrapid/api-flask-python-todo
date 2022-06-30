from .flask_config import app
from dotenv import load_dotenv
import os
load_dotenv()

# configuring the database
app.config['SQLALCHEMY_DATABASE_URI'] = f"{os.getenv('engine_name')}://{os.getenv('myuser')}:{os.getenv('mypass')}@{os.getenv('ip')}:{os.getenv('port_name')}/{os.getenv('db_name')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

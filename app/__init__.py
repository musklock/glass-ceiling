from flask import Flask
from config import Config


app = Flask(__name__, template_folder='../templates')
app.config.from_object(Config)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

from app import routes, models

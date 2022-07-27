from flask import Flask
from config import Config


from .poke.routes import poke

app = Flask(__name__)


app.register_blueprint(poke)

app.config.from_object(Config)


from .models import db

db.init_app(app)

from . import routes
from . import models
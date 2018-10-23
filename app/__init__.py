from flask import Flask
from instance.config import DevelopmentConfig,ProductionConfig

app = Flask(__name__)
app.config.from_object(ProductionConfig)

from .views import *
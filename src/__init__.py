"""initialise app"""

from flask import Flask

app = Flask(__name__)

from src import routes

from flask import Blueprint

bp = Blueprint('administrator', __name__)

from app.administrator import routes

from . import main
from ..models import *
from flask import render_template


@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html')

import os
from flask import Blueprint, render_template

main_page = Blueprint("main_page", __name__)


@main_page.route('/', methods=['GET'])
def index():
    return open("../../templates/index.html").read()

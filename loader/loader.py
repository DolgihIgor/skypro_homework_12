from flask import Blueprint, render_template, request
from functions import load_posts
POST_PATH = 'posts.json'

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


# @loader_blueprint.route('/search/')
# def loader():

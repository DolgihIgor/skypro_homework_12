from flask import Blueprint, render_template, request
from functions import load_posts
POST_PATH = 'posts.json'

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/post/', methods=['GET', 'POST'])
def post():
    picture = request.files.
    print(picture)
    return render_template('post_form.html')


@loader_blueprint.route('/uploaded/', methods=['GET', 'POST'])
def uploaded():
    picture = request.files.get('picture')
    print(picture.filename)
    return render_template('post_uploaded.html')

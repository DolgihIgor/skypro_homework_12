from flask import Blueprint, render_template, request
from functions import load_posts, search_posts
POST_PATH = 'posts.json'

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


@main_blueprint.route('/search/')
def loader():
    search_request = request.args['s']
    search_result = search_posts(search_request, POST_PATH)
    return render_template('post_list.html', search_request=search_request, search_posts=search_result)



from flask import Blueprint, render_template, request
from functions import load_posts, uploads_post
POST_PATH = 'posts.json'

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates', static_folder='static')


@loader_blueprint.route('/post/', methods=['GET', 'POST'])
def post():
    return render_template('post_form.html')


@loader_blueprint.route('/uploaded/', methods=['GET', 'POST'])
def upload():
    picture = request.files.get('picture')
    filename = picture.filename
    picture.save(f"/static/{filename}")
    content = request.values.get('content')
    posts = load_posts(POST_PATH)
    posts.append({
        'pic': f'uploads/images/{filename}',
        'content': content
    })

    return render_template('post_uploaded.html', content=content)

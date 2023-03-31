import json


def load_posts(path):
    """ Функция для загрузки всех постов из json """
    with open(path,'r', encoding='utf-8') as file:
        posts = json.load(file)
    return posts


def search_posts(search_request, path):
    """Функция для поиска постов по ключевому слову"""
    result_posts = []
    posts = load_posts(path)
    for post in posts:
        if search_request.lower() in post['content'].lower():
            result_posts.append(post)
    return result_posts


def uploads_post(post, path):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(post, file)
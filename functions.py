import json

def load_posts(path):
    with open(path,'r', encoding='utf-8') as file:
        posts = json.load(file)
    return posts

from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {"username": 'Gitau'}
    posts = [
        {
            'author': {'username': 'Rahima'},
            'body': 'This is a test'
        },
        {
            'author': {'username': 'Gitau'},
            'body': 'This is another test'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

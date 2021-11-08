from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {"username": "Harry"}
    posts = [
        {
            'author': {'username': 'Gitau'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Rahima'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

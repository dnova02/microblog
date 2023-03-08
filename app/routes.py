from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Dariel'}
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''

from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''


from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': "Dariel"}
    posts = [
        {
             'author': {'username': 'Brian'},
             'body': 'Beautiful day in Washington!'
        },
        {
             'author': {'username': 'Makayla'},
             'body': 'The Last of Us show is so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
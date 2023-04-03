from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Dariel'}
    posts = [
        {
            'author': {'username': 'Brian'},
            'body': "I'm obsessed with Ready Or Not"
        },
        {
            'author': {'username': 'Makayla'},
            'body': "I play Sims 4"
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


from flask import render_template
from app import app
from app.forms import LoginForm

# ..

from flask import render_template, flash, redirect, url_for

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for user {}, remember_me{}".format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title="Sign In", form=form)
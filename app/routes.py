from flask import render_template
from app import app
from flask_login import current_user, login_user
from flask import render_template
from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for
from app.models import User

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

@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_username(form.username.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        flash("Login requested for user {}, remember_me{}".format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title="Sign In", form=form)
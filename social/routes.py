from flask import render_template, url_for, request, flash, redirect, Response
from flask_login import current_user, login_user
from werkzeug.security import check_password_hash
from social.forms import LoginForm
from database.model import DB
from social.models import User, get_user
from social import app


# Default page
@app.route('/')
@app.route('/index')
def index():
    if "username" in request.args:
        user = {'username': request.args["username"]}
    else:
        user = {'username': ""}
    
    raw_posts = DB.get("select user_id, body, timestamp from posts ORDER BY timestamp desc limit 15")

    posts = [{
                "author": {"username": DB.get("select username from user_info where user_id=%s", [post[0]], one=True)[0]},
                "body": post[1]} 
                for post in raw_posts]

    return render_template('home_page.html', title='Home', user=user, posts=posts)


@app.route('/login', methods = ["GET", "POST"])
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()

    if request.method == "POST":
        if form.validate_on_submit():
            user = get_user(form.username.data)
            if not user:
                flash('User {} not registered'.format(form.username.data))

            else:
                if not user.check_password_hash(form.password.data):
                    flash("Wrong username or password")

                else:
                    flash("You logged in as {}".format(form.username.data))
                    return redirect('/index')
        else:
            pass
            # flash('Data not valid')
        
    return render_template('login.html', title='Sign In', form=form)

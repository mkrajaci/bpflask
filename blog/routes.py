from flask import render_template, url_for, flash, redirect
from blog import app, db, bcrypt
from blog.forms import RegistrationForm, LoginForm
from blog.models import User, Post
from flask_login import login_user, current_user, logout_user

posts = [
    {
        'author': 'Mario Krajačić',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': '18.09.2018.'
    },
    {
        'author': 'Mario Krajačić',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': '19.09.2018.'
    }
]

# rute do stranica
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register', methods=['get', 'post'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email= form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Acount created {form.username.data}!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['get', 'post'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def login():
    logout_user()
    return redirect(url_for('home'))

#TODO: https://youtu.be/CSHx6eCkmv0?t=34m36s
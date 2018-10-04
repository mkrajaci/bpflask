from flask import render_template, url_for, flash, redirect
from blog import app
from blog.forms import RegistrationForm, LoginForm
from blog.models import User, Post

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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['get', 'post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password')
    return render_template('login.html', title='Login', form=form)
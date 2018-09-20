from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'f9a44d6fa3d1c2ca1eca9837c452aa8a'

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
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

#TODO: Sloziti flash poruku, https://youtu.be/UIJKdCIEXUQ?t=42m10s
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
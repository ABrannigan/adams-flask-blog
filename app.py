from flask import Flask, render_template, url_for, redirect, flash
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from boto.s3.connection import S3Connection
import os

app = Flask(__name__)

# local
 # with open('secret.txt', 'r') as secret:
 #     app.config['SECRET_KEY'] = secret.read()
app.config['SECRET_KEY'] = os.environ.get('S3_KEY')
# Heroku
#app.config['SECRET_KEY'] = S3Connection(os.environ['S3_KEY'])
# s3 = S3Connection(os.environ['S3_KEY'], os.environ['S3_SECRET'])
# app.config['SECRET_KEY'] = s3.S3_KEY



posts = [
        {'author': 'Adam Brannigan',
         'title': 'blog post 1',
         'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Repellendus voluptatibus necessitatibus laborum, officiis reprehenderit beatae suscipit, natus in incidunt possimus sequi adipisci a, excepturi vitae odio, porro cum saepe est.',
         'date': '24 Jan 2018',
         'category': 'Design',
         'image': 'design.jpg'
        },
        {'author': 'Dayna O\'Reilly',
         'title': 'blog post 2',
         'content': 'Lorem ipsum dolor sit amet,consectetur adipisicing elit. Repellendus voluptatibus necessitatibus laborum, officiis reprehenderit beatae suscipit, natus in incidunt possimus sequi adipisci a, excepturi vitae odio, porro cum saepe est.',
         'date': '2 Aug 2018',
         'category': 'Codeing',
         'image': 'coding.jpg'
        }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}','success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)



@app.route('/login', methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'ab-139@hotmail.com' and form.password.data == 'qwertyui':
            flash(f'Hello {form.email.data} you are now logged in!','success')
            return redirect(url_for('home'))
        else:
            flash(f'Invalid credentials please check Username and Password','danger')

    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run()

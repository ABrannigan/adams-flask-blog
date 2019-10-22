from flask import Flask, render_template, url_for
app = Flask(__name__)
# app.config['DEBUG'] = True

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

if __name__ == '__main__':
    app.run()

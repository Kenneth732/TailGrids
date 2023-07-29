from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = '85d597d573ec0aff9812da3f5386a743ac0d85fb03e59896'

messages = [{'title': 'Python3',
             'content': 'Very straight-to-point article. Really worth time reading. Thank you! But tools are just the instruments for the UX designers. The knowledge of the design tools are as important as the creation of the design strategy.'},
            {'title': 'Understanding Javascript',
             'content': 'The article covers the essentials, challenges, myths and stages the UX designer should consider while creating the design strategy.'}
            ]

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            messages.append({ 'title': title, 'content': content })
            return redirect(url_for('index'))
    return render_template('create.html')

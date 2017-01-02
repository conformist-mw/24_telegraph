from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import json
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    author = db.Column(db.String(80))
    body = db.Column(db.Text)
    post_id = db.Column(db.String(10))

    def __init__(self, title, author, body, post_id):
        self.title = title
        self.author = author
        self.body = body
        self.post_id = post_id

    def __repr__(self):
        return 'Post(title={}, author={}, body={}, post_id={}'.format(
            self.title, self.author, self.body, self.post_id)


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/telegraph', methods=['POST'])
def telegraph():
    title = request.form['header']
    author = request.form['signature']
    body = request.form['body']
    post_id = request.cookies['id']
    new_post = Post(title, author, body, post_id)
    db.session.add(new_post)
    db.session.commit()
    return json.dumps({'status': 'ok', 'path': post_id})


@app.route('/<post_id>', methods=['GET', 'POST'])
def show_post(post_id):
    post = Post.query.filter_by(post_id=post_id).first()
    data = {'author': post.author,
            'title': post.title,
            'body': post.body,
            'post_id': post.post_id}
    if request.cookies.get('id') == post_id:
        return render_template('auth.html', **data)
    else:
        return render_template('anonymous.html', **data)


@app.route('/<post_id>/edit', methods=['GET', 'POST'])
def edit_post(post_id):
    post = Post.query.filter_by(post_id=post_id).first()
    data = {'author': post.author,
            'title': post.title,
            'body': post.body,
            'post_id': post.post_id}
    return render_template('edit.html', **data)


@app.route('/save_post', methods=['POST'])
def save_post():
    title = request.form['header']
    author = request.form['signature']
    body = request.form['body']
    post_id = request.cookies['id']
    post = Post.query.filter_by(post_id=post_id).first()
    post.title = title
    post.author = author
    post.body = body
    db.session.commit()
    return json.dumps({'status': 'ok', 'path': post_id})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


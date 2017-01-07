from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


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


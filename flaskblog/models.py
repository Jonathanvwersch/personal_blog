from flaskblog import db
from datetime import datetime

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    url_title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    author = db.Column(db.String(100), nullable=False)
    summary = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    field = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(1000), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    url_title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    summary = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    field = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(1000), nullable=False)
    thumbnail = db.Column(db.String(1000), nullable=False)

    def __repr__(self):
        return f"Project('{self.title}')"
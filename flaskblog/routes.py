from flask import render_template, url_for, flash, redirect, request
from flaskblog import app
from flaskblog.models import Post
from flaskblog import db

@app.route("/")
def home():
    return render_template('home.html', title = 'Jvw')

@app.route("/blog")
def blog():
    post = Post.query.all()
    return render_template('blog.html', title = 'Blog ✍️', posts=post)

@app.route("/blog/<int:post_id>/<string:post_url_title>")
def blog_post(post_url_title, post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('blog_post.html', title=post.title, post=post)

@app.route("/add")
def add():
    return render_template('add.html')

@app.route("/addpost", methods=['POST'])
def addpost():
    title= request.form['title']
    url_title= request.form['url_title']
    summary=request.form['summary']
    author=request.form['author']
    content=request.form['content']
    image= request.form['image']
    post=Post(title=title, url_title=url_title, summary=summary, author=author, image=image, content=content)
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('blog'))
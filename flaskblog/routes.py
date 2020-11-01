from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.models import Post

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

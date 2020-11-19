from flask import render_template, url_for, flash, redirect, request, session, abort
from flaskblog import app
from flaskblog.models import Post
from flaskblog import db
from flaskblog import admin
from flask_admin.contrib.sqla import ModelView
from sqlalchemy import desc

class SecureModelView(ModelView):
    def is_accessible(self):
        if "logged_in" in session:
            return True
        else:
            abort(403)

admin.add_view(SecureModelView(Post, db.session))

content = "Hi, I'm Jonathan and I like to build things. On this site you can find my blog where I write about whatever interests me in the moment"

@app.route("/")
def home():
    return render_template('home.html', title = 'Jonathan van Wersch', content=content)

@app.route("/blog")
def blog():
    post = Post.query.order_by(Post.date_posted.desc())
    return render_template('blog.html', title = 'Blog', post=post, content=content)

@app.route("/blog/<int:post_id>/<string:post_url_title>")
def blog_post(post_url_title, post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('blog_post.html', title=post.title, post=post, content=post.summary)


# @app.route("/projects")
# def blog():
#     post = Post.query.order_by(Post.date_posted.desc())
#     return render_template('blog.html', title = 'Blog', post=post, content=content)

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        file_password = open("flaskblog/password.txt","r") 
        password = file_password.read()
        file_password.close()

        file_username = open("flaskblog/username.txt","r") 
        username = file_username.read()
        file_username.close()

        if request.form.get("username") == username and request.form.get("password") == password:
            session['logged_in'] = True
            return redirect("/admin")
        else: 
             return render_template('/login.html', failed=True, title="Login")
    return render_template('/login.html', title="Login") 

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
    
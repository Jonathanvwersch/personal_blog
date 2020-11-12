from flask import render_template, url_for, flash, redirect, request, session, abort
from flaskblog import app
from flaskblog.models import Post
from flaskblog import db
from flaskblog import admin
from flask_admin.contrib.sqla import ModelView

class SecureModelView(ModelView):
    def is_accessible(self):
        if "logged_in" in session:
            return True
        else:
            abort(403)

admin.add_view(SecureModelView(Post, db.session))

@app.route("/")
def home():
    return render_template('home.html', title = 'Jonathan van Wersch')

@app.route("/blog")
def blog():
    post = Post.query.all()
    return render_template('blog.html', title = 'Blog', post=post)

@app.route("/blog/<int:post_id>/<string:post_url_title>")
def blog_post(post_url_title, post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('blog_post.html', title=post.title, post=post)

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form.get("username") == "Jonathanvw" and request.form.get("password") == "1234":
            session['logged_in'] = True
            return redirect("/admin")
        else: 
             return render_template('/login.html', failed=True, title="Login")
    return render_template('/login.html', title="Login") 

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
    

# @app.route("/add")
# def add():
#     return render_template('add.html')

# @app.route("/addpost", methods=['POST'])
# def addpost():
#     title= request.form['title']
#     url_title= request.form['url_title']
#     summary=request.form['summary']
#     author=request.form['author']
#     content=request.form['content']
#     image= request.form['image']
#     post=Post(title=title, url_title=url_title, summary=summary, author=author, image=image, content=content)
#     db.session.add(post)
#     db.session.commit()
#     return redirect(url_for('blog'))
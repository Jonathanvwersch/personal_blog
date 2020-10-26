from flask import Flask, render_template, url_for
app = Flask(__name__)

blog_posts = [
    {
        'author': 'Jonathan van Wersch',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'April 20, 2018'
    },

    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'April 21, 2018'
    },
]

@app.route("/")
@app.route("/starthere")
def home():
    return render_template('home.html', title = 'Jvw')

@app.route("/blog")
def blog():
    return render_template('blog.html', title = '✍️ Blog', posts=blog_posts)

if __name__ == '__main__':
    app.run(debug=True)


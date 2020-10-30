from flask import Flask, render_template, url_for
app = Flask(__name__)

blog_posts = [
    {
        'author': 'Jonathan van Wersch',
        'title': "Reviewing Udacity's C++ Nanodegree",
        'url-title': "Reviewing Udacity's Cpp Nanodegree",
        'content': "Learning C++ can open up careers in a wide array of fields ranging from robotics to game programming, but at a cost of about $1000, is Udacity's nanodegree the best way to learn it?",
        'date_posted': 'October 31, 2020',
        'thumbnail': "https://upload.wikimedia.org/wikipedia/commons/1/18/ISO_C%2B%2B_Logo.svg" 
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


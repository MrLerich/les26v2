from flask import Flask, render_template
from bp_posts.views import bp_posts

app = Flask(__name__)
app.register_blueprint(bp_posts)


# @app.route('/')
# def index():
#     return 'It works'

if __name__ == '__main__':
    app.run(debug=True)

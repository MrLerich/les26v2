from flask import Flask, render_template, Blueprint
from config import DATA_PATH_POSTS
from bp_posts.dao.post_dao import PostDAO


bp_posts = Blueprint("bp_posts", __name__, template_folder="templates")

post_dao = PostDAO(DATA_PATH_POSTS)

@bp_posts.route("/")
def page_posts_index():
    all_posts = post_dao.get_all()
    return render_template("posts_index.html", posts=all_posts)


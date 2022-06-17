from flask import Flask, render_template, Blueprint
from werkzeug.exceptions import abort

from bp_posts.dao.comment import Comment
from bp_posts.dao.comment_dao import CommentDAO
from bp_posts.dao.post_dao import PostDAO
from config import DATA_PATH_POSTS, DATA_PATH_COMMENTS

###Создаем blueprint
bp_posts = Blueprint("bp_posts", __name__, template_folder="templates")

###Создаем объекты доступа к данным из config
post_dao = PostDAO(DATA_PATH_POSTS)
comment_dao = CommentDAO(DATA_PATH_COMMENTS)


@bp_posts.route("/")
def page_posts_index():
    '''Страница всех постов'''
    all_posts = post_dao.get_all()
    return render_template("posts_index.html", posts=all_posts)


@bp_posts.route("/posts/<int:pk>/")
def page_posts_single(pk: int):
    '''Страница одного поста'''
    post: Post | None = post_dao.get_by_pk(pk)
    comments: list[Comment] = comment_dao.get_comments_by_post_pk(pk)

    if post is None:
        abort(404)

    return render_template("posts_single.html",
                           post=post,
                           comments=comments,
                           comments_len=len(comments)
                           )

bp_posts.route("/users/<username>")
def page_posts_by_user(username: str):
    posts = post_dao.get_by_poster(username)

    return render_template("posts_user-feed.html",
                           posts=posts,
                           username=username
                           )
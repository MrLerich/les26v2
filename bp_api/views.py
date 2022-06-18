from flask import Blueprint, jsonify
from bp_posts.dao.comment import Comment
from bp_posts.dao.comment_dao import CommentDAO
from bp_posts.dao.post import Post
from bp_posts.dao.post_dao import PostDAO

from config import DATA_PATH_POSTS, DATA_PATH_COMMENTS

###Создаем blueprint
bp_api = Blueprint("bp_api", __name__)

###Создаем объекты доступа к данным из config
post_dao = PostDAO(DATA_PATH_POSTS)
comment_dao = CommentDAO(DATA_PATH_COMMENTS)


@bp_api.route("/")
def api_doc():
    return "по / в api должно лежать что-то типа документации, for frontend: /api/posts  /api/posts/pk"

@bp_api.route("/posts/")
def api_post_all():
    """"Endpoint Будет возвращать все посты"""
    all_posts =post_dao.get_all()
    return jsonify(all_posts)

@bp_api.route("/posts/<int:pk>")
def api_post_single(pk: int):
    """"Endpoint Возвращает один  конкретный пост"""
    post: Post | None = post_dao.get_by_pk(pk)
    return jsonify(post)

@bp_api.route("")
def api_comment_post()
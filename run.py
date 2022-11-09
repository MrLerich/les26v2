from flask import Flask

from bp_api.views import bp_api
from bp_posts.views import bp_posts
from exceptions.data_exceptions import DataSourceError

import config_logger

app = Flask(__name__)
def create_and_config_app(config_path):
    """Создание и конфиги нашего приложения"""


    app.register_blueprint(bp_posts)
    app.register_blueprint(bp_api, url_prefix="/api")  # все что начинается api будет обрабатываться
    app.config.from_pyfile(config_path)
    config_logger.config(app)
    app.config['JSON_AS_ASCII'] = False  # кодировка проти в аляберды
    app.config['JSON_SORT_KEYS'] = False  # против сортировки

    return app

app = create_and_config_app("config.py")



@app.errorhandler(404)
def page_error_404(error):
    return f"Такой страницы нет! {error}", 404


@app.errorhandler(500)
def page_error_500(error):
    return f"На сервере произошла ошибка - {error}", 500


@app.errorhandler(DataSourceError)
def page_error_data_source_error(error):
    return f"Ошибка, связанная с данными: {error}", 500


if __name__ == '__main__':
    app.run()

from flask import Flask, render_template
from bp_posts.views import bp_posts
from exceptions.data_exceptions import DataSourceError


def create_and_config_app(config_path):

    app = Flask(__name__)
    app.register_blueprint(bp_posts)
    app.config.from_pyfile(config_path)
    return app
app = create_and_config_app("config.py")


@app.errorhandler(404)
def page_error_404(error):
    return "Такой страницы нет!", 404


@app.errorhandler(500)
def page_error_500(error):
    return f"На сервере произошла ошибка - {error}", 500


@app.errorhandler(DataSourceError)
def page_error_data_source_error(error):
    return f"Ошибка, связанная с данными: {error}", 500

if __name__ == '__main__':
    app.run(debug=True)

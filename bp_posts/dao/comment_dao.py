# класс который будет делать все манипуляции с нашими данными комментариев
import json
from json import JSONDecodeError

from exceptions.data_exceptions import DataSourceError
from bp_posts.dao.comment import Comment


class CommentDAO:
    '''Менеджер абстракции комментариев'''
    def __init__(self, path):
        self.path = path

    def _load_data(self):
        '''Загружает данные из JSON и возвращает список словарей'''

        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                posts_data = json.load(file)
        except (FileNotFoundError, JSONDecodeError):
            raise DataSourceError(f'Не удалось получить данные из файла. Проверьте источник данных.')

        return posts_data

    def _load_comments(self) -> list[Comment]:
        ''' Возращает список элементов Comment '''

        comments_data = self._load_data()
        comments = [Comment(**comment_data) for comment_data in comments_data]
        return comments

    def get_comments_by_post_pk(self, post_pk) -> list[Comment]:
        '''  Получает все комментарии к посту по его post_pk '''
        comments = self._load_comments()

        comments_mathing = [c for c in comments if c.post_pk == post_pk]

        return comments_mathing


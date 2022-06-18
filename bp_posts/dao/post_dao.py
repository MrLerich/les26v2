# класс который будет делать все манипуляции с нашими данными постов

import json
from json import JSONDecodeError

from bp_posts.dao.post import Post
from exceptions.data_exceptions import DataSourceError


class PostDAO:
    '''Менеджер абстракции постов'''

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

    def _load_posts(self) -> list[Post]:
        '''Возвращает список экземпляров Post'''

        posts_data = self._load_data()
        list_of_posts = [Post(**post_data) for post_data in posts_data]

        return list_of_posts

    def get_all(self) -> list[Post]:
        '''Получает все посты'''

        posts = self._load_posts()

        return posts

    def get_by_pk(self, pk: int) -> Post:
        '''Получает пост по его pk'''

        if type(pk) != int:
            raise TypeError('pk должен быть числом')

        posts = self._load_posts()

        # post = [post for post in posts if post.pk == pk] #возвращает list, а нужно Post
        for post in posts:
            if post.pk == pk:
                return post

    def search_by_content(self, substring: str) -> list[Post]:
        '''Ищет посты, по входящему в него контенту(substring)'''

        if type(substring) != str:
            raise TypeError('substring должен быть стоковым значением')

        substring: str = substring.lower()

        posts = self._load_posts()
        matching_posts = [post for post in posts if substring in post.content.lower()]

        return matching_posts

    def get_by_poster(self, user_name: str) -> list[Post]:
        '''Получает все посты пользователя'''
        if type(user_name) != str:
            raise TypeError('username должен быть стоковым значением')

        user_name: str = user_name.lower()

        posts = self._load_posts()

        matching_posts = [post for post in posts if post.poster_name.lower() == user_name]

        return matching_posts

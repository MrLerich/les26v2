# класс который хранит данные о посте "абстракция поста"
class Post:
    '''Абстракция постов для использования в DAO'''
    def __init__(self,
                 pk: int = 0,
                 poster_name: str = '',
                 poster_avatar='',
                 pic='',
                 content: str = '',
                 views_count: int = 0,
                 likes_count: int = 0
                 ):
        self.pk = pk
        self.poster_name = poster_name
        self.poster_avatar = poster_avatar
        self.pic = pic
        self.content = content
        self.views_count = views_count
        self.likes_count = likes_count

    def __repr__(self):
        return f'Post(' \
               f'{self.pk}, ' \
               f'{self.poster_name}, ' \
               f'{self.poster_avatar}, ' \
               f'{self.pic}, ' \
               f'{self.content}, ' \
               f'{self.views_count}, ' \
               f'{self.likes_count}, ' \
               f')'




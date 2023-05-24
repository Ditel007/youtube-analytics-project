import json
import os

from googleapiclient.discovery import build

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('YT_API_KEY')

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API
        self.__channel_id - id канала
        self.title - название канала
        self.description - описание канала
        self.url - ссылка на канал
        self.subscribers_count - количество подписчиков
        self.video_count - количество видео
        self.views_count - общее количество просмотров"""
        self.__channel_id = channel_id
        self.title = self.get_channel()['items'][0]['snippet']['title']
        self.description = self.get_channel()['items'][0]['snippet']['description']
        self.url = f'https://www.youtube.com/channel/{self.__channel_id}'
        self.subscribers_count = int(self.get_channel()['items'][0]['statistics']['subscriberCount'])
        self.video_count = int(self.get_channel()['items'][0]['statistics']['videoCount'])
        self.views_count = int(self.get_channel()['items'][0]['statistics']['viewCount'])

    def __str__(self):
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        return self.subscribers_count + other.subscribers_count

    def __sub__(self, other):
        return self.subscribers_count - other.subscribers_count

    def __lt__(self, other):
        return self.subscribers_count < other.subscribers_count

    def __le__(self, other):
        return self.subscribers_count <= other.subscribers_count

    def __gt__(self, other):
        return self.subscribers_count > other.subscribers_count

    def __ge__(self, other):
        return self.subscribers_count >= other.subscribers_count

    @property
    def channel(self):
        """Возвращает название канала."""
        return youtube.channels()

    def get_channel(self):
        """Возвращает список словарей, для работы с ключами и значениями"""
        channel = self.channel.list(id=self.__channel_id, part='snippet,statistics').execute()
        return channel

    def print_info(self):
        """Выводит в консоль информацию о канале."""
        channel = self.channel.list(id=self.__channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    @property
    def channel_id(self) -> str:
        """Геттер возвращает id канала."""
        return self.__channel_id

    @channel_id.setter
    def channel_id(self, value):
        """Сеттер возвращает id канала."""
        print("AttributeError: property 'channel_id' of 'Channel' object has no setter")

    @classmethod
    def get_service(cls):
        """Класс-метод возвращает объект для работы с YouTube API."""
        return cls.youtube

    def to_json(self, filename) -> None:
        """Метод возвращает в json значения атрибутов экземпляра Channel."""
        data = {
            'channel_id': self.__channel_id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscribers_count': self.subscribers_count,
            'video_count': self.video_count,
            'views_count': self.views_count
        }
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

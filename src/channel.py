import json
import os

from googleapiclient.discovery import build

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('YT_API_KEY')

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self._channel_id = channel_id

    @property
    def channel(self):
        """Возвращает название канала."""
        return youtube.channels()

    def print_info(self):
        """Выводит в консоль информацию о канале."""
        channel = self.channel.list(id=self._channel_id, part='snippet,statistics').execute()
        print(f"Название канала: {channel['items'][0]['snippet']['title']}")
        print(f"Количество видео: {int(channel['items'][0]['statistics']['videoCount'])}")
        print(f"Ссылка на канал: https://www.youtube.com/channel/{self._channel_id}")

from src.channel import Channel


class Video:
    """
    __v_id - id видео
    __v_name - название видео
    __v_link - ссылка на видео
    __v_views - количество просмотров
    __v_likes - количество лайков
    """

    def __init__(self, v_id):
        self.__v_id = v_id
        self.__video = Channel.get_video(self.__v_id)
        self.__v_name = self.__video['items'][0]['snippet']['title']
        self.__v_link = f'https://www.youtube.com/watch?v={self.__v_id}'
        self.__v_views = self.__video['items'][0]['statistics']['viewCount']
        self.__v_likes = self.__video['items'][0]['statistics']['likeCount']

    @property
    def title(self):
        return self.__v_name

    @property
    def id_video(self):
        return self.__v_id

    @property
    def url(self):
        return self.__v_link

    @property
    def views_count(self):
        return self.__v_views

    @property
    def likes_count(self):
        return self.__v_likes

    def __str__(self):
        return self.__v_name


class PLVideo(Video):
    def __init__(self, id_video, playlist_id):
        super().__init__(id_video)
        self.__playlist_id = playlist_id

    @property
    def playlist_id(self):
        return self.__playlist_id

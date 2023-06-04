from src.channel import Channel


class PlayList:
    def __init__(self, playlist_id):
        self.__playlist_id = playlist_id
        self.__playlist = Channel.get_playlist(self.__playlist_id)
        self.__duration = Channel.get_videos_duration(self.__playlist_id)
        self.__videos_in_playlist = Channel.get_videos_in_playlist(self.__playlist_id)
        self.__title = self.__playlist['items'][0]['snippet']['title']
        self.__url = f'https://www.youtube.com/playlist?list={self.__playlist_id}'

    @property
    def title(self):
        return self.__title

    @property
    def url(self):
        return self.__url

    @property
    def total_duration(self):
        return self.__duration

    def show_best_video(self):
        most_liked_video = max(self.__videos_in_playlist, key=lambda x: int(x["statistics"]["likeCount"]))
        return f"https://youtu.be/{most_liked_video['id']}"

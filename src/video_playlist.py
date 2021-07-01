"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""
    
    def __init__(self, name: str, videos: list):
        self.name = name
        self.videos = []


    def get_name(self):
        """Returns name of the playlist """

        return self.name 

    def get_videos(self):
        """Return list of videos in playlist """

        return self.videos

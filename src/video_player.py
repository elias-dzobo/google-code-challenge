"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist
import random 

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._playlist = {}
        self.currently_playing = False 
        self.paused = False
        self.video_playing = None

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print("{} videos in the library".format(num_videos))

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        vid_list = sorted(self._video_library.get_all_videos(), key = lambda v: v._title)
        for video in vid_list:
            if video._flag == "":
                tag = ' '.join(list(video._tags))
                print(" {} ({}) [{}]".format(video._title, video._video_id, tag))
            else:
                tag = ' '.join(list(video._tags))
                print(" {} ({}) [{}] - FLAGGED (reason: {})".format(video._title, video._video_id, tag, video._flag))

        #print("show_all_videos needs implementation")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        video = self._video_library.get_video(video_id)
        if video == None:
            print("Cannot play video: Video does not exist")
        elif video._flag != "":
            print("Cannot play video: Video is currently flagged (reason: {})".format(video._flag))
        elif self.currently_playing == False:
            self.video_playing = video
            self.paused = False
            print("Playing video: {}".format(video._title))
            self.currently_playing = True 
        else:
            self.stop_video() 
            self.play_video(video_id) 

        #print("play_video needs implementation")

    def stop_video(self):
        """Stops the current video."""
        if self.video_playing == None:
            print("Cannot stop video: No video is currently playing")
        else:
            print("Stopping video: {}".format(self.video_playing._title))
            self.currently_playing = False 
            self.video_playing = None
        #print("stop_video needs implementation")

    def play_random_video(self):
        """Plays a random video from the video library."""
        if self.currently_playing == True:
            self.stop_video()
        video_list = [vid for vid in list(self._video_library.get_all_videos()) if vid._flag == ""]
        if len(video_list) == 0:
            print("No videos available")
        else:
            video = random.choice(video_list)
            self.play_video(video.video_id)
        #print("play_random_video needs implementation")

    def pause_video(self):
        """Pauses the current video."""
        if self.paused == True:
            print("Video already paused: {}".format(self.video_playing._title))
        elif self.currently_playing == False:
            print("Cannot pause video: No video is currently playing")
        else:
            print("Pausing video: {}".format(self.video_playing._title))
            self.paused = True 
        #print("pause_video needs implementation")

    def continue_video(self):
        """Resumes playing the current video."""
        if self.currently_playing == False:
            print("Cannot continue video: No video is currently playing")
        elif self.paused == True:
            print("Continuing video: {}".format(self.video_playing._title))
            self.paused = False
            self.currently_playing = True 
        else:
            print("Cannot continue video: Video is not paused")
        #print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""
        if self.video_playing == None:
            print("No video is currently playing")
        else:
            tag = ' '.join(list(self.video_playing._tags))
            if self.paused == True:
                print("Currently playing: {} ({}) [{}] - PAUSED".format(self.video_playing._title, self.video_playing._video_id, tag))
            else:
                print("Currently playing: {} ({}) [{}]".format(self.video_playing._title, self.video_playing._video_id, tag))
        #print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() in list(map(str.lower, list(self._playlist.keys()))):
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            playlist = Playlist(playlist_name, [])
            self._playlist[playlist_name.lower()] = playlist
            print("Successfully created new playlist: {}".format(playlist_name))
        #print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        video = self._video_library.get_video(video_id)
        if video == None and (playlist_name.lower() not in list(map(str.lower, list(self._playlist.keys())))):
            print("Cannot add video to {}: Playlist does not exist".format(playlist_name))
        elif video == None:
            print("Cannot add video to {}: Video does not exist".format(playlist_name))
        elif video._flag != "":
            print("Cannot add video to {}: Video is currently flagged (reason: {})".format(playlist_name, video._flag))
        elif playlist_name.lower() not in list(map(str.lower, list(self._playlist.keys()))):
            print("Cannot add video to {}: Playlist does not exist".format(playlist_name))
        elif video_id in self._playlist[playlist_name.lower()].get_videos():
            print("Cannot add video to {}: Video already added".format(playlist_name))
        else:
            playlist = self._playlist[playlist_name.lower()]
            playlist.videos.append(video_id)
        #print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""
        if len(self._playlist) == 0:
            print("No playlists exist yet")
        else:
            print("Showing all playlists:")
            play_list = sorted(list(self._playlist.values()), key = lambda x: x.name)
            for playlist in play_list:
                print(playlist.name)

        #print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        lower_name = playlist_name.lower()
        if lower_name not in list(map(str.lower, list(self._playlist.keys()))):
            print("Cannot show playlist {}: Playlist does not exist".format(playlist_name))
        else:
            print("Showing playlist: {}".format(playlist_name))
            if len(self._playlist[lower_name].videos) == 0:
                print("No videos here yet")
            else:
                playlist = self._playlist[lower_name]
                for video in playlist.get_videos():
                    video = self._video_library.get_video(video)
                    if video._flag != "":
                        print(" {} ({}) {} - FLAGGED (reason: {})".format(video._title, video._video_id, video._tags, video._flag))
                    else:
                        print(" {} ({}) {}".format(video._title, video._video_id, video._tags))
        #print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        lower_name = playlist_name.lower()
        if lower_name not in list(map(str.lower, list(self._playlist.keys()))):
            print("Cannot remove video from {}: Playlist does not exist".format(playlist_name))
        elif video_id not in self._playlist[lower_name].get_videos():
            print("Cannot remove video from {}: Video is not in playlist".format(playlist_name))
        else:
            print("Removed video from {}: {}".format(playlist_name, self._video_library.get_video(video_id)._title))
            self._playlist[lower_name].videos.remove(video_id)
        #print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() not in list(map(str.lower, list(self._playlist.keys()))):
            print("Cannot clear playlist {}: Playlist does not exist".format(playlist_name))
        else:
            self._playlist[playlist_name].videos = []
            print("Successfully removed all videos from {}".format(playlist_name))

        #print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name not in list(self._playlist.keys()):
            print("Cannot delete playlist {}: Playlist does not exist".format(playlist_name))
        else:
            del self._playlist[playlist_name]
            print("Deleted playlist: {}".format(playlist_name))
        #print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        query_result = [video for video in list(self._video_library.get_all_videos()) if search_term.lower() in video._title.lower() and video._flag == ""]
        if len(query_result) == 0:
            print("No search results for {}".format(search_term))
        else:
            print("Here are the results for {}:".format(search_term))
            count = 1
            for video in query_result:
                tag = ' '.join(list(video._tags))
                print("{}) {} ({}) [{}]".format(count, video._title, video._video_id, tag))
                count += 1
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            play_choice = input("Enter video number: ")
            try:
                play_choice = int(play_choice)
                if int(play_choice) <= count:
                    vid = query_result[play_choice-1]
                    self.play_video(vid._video_id)
            except:
                quit 
        #print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        query_result = [vid for vid in self._video_library.get_all_videos() if video_tag in list(vid._tags) and vid._flag == ""]
        if len(query_result) == 0:
            print("No search results for {}".format(video_tag))
        else:
            print("Here are the results for {}:".format(video_tag))
            count = 1
            for video in query_result:
                tag = ' '.join(list(video._tags))
                print("{}) {} ({}) [{}]".format(count, video._title, video._video_id, tag))
                count += 1
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            play_choice = input("Enter video number: ")
            try:
                play_choice = int(play_choice)
                if int(play_choice) <= count:
                    vid = query_result[play_choice-1]
                    self.play_video(vid._video_id)
            except:
                quit 
        #print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        video = self._video_library.get_video(video_id)
        if video == None:
            print("Cannot flag video: Video does not exist")
        else:
            if video._flag != "":
                print("Cannot flag video: Video is already flagged")
            else:
                if self.video_playing != None and self.video_playing._video_id == video_id:
                        self.stop_video()
                if flag_reason == "":
                    flag_reason = "Not supplied"
                    video._flag = flag_reason
                    print("Successfully flagged video: {} (reason: {})".format(video._title, flag_reason))
                else:
                    video._flag = flag_reason
                    print("Successfully flagged video: {} (reason: {})".format(video._title, flag_reason))

        #print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        video = self._video_library.get_video(video_id)
        if video == None:
            print("Cannot remove flag from video: Video does not exist")
        elif video._flag == "":
            print("Cannot remove flag from video: Video is not flagged")
        else:
            video._flag = ""
            print("Successfully removed flag from video: {}".format(video._title))
        print("allow_video needs implementation")

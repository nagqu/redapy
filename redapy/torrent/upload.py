from dataclasses import asdict
import os
from typing import List, Union
from redapy.base import BaseAuth, TorrentUpload, urls, mappings_categories, mappings_release, mappings_artist_importance


# No Log support for now

class Upload():
    def __init__(self):
        self.sess = BaseAuth()
        self.url: str = urls["base_url"] + urls["torrent_up"]

    def prepare_torrent(self, category: Union[str, int], artists: List[str], importance: Union[List[str], List[int]],
                        title: str, year: int, release_type: Union[str, int],
                        format: str, bitrate: str, media: str, tags: List[str],
                        image: str, album_desc: str, torrent_desc: str, **kwargs):
        if type(category) == str:
            category: int = [
                i for i in mappings_categories if mappings_categories[i] == category][0]

        if type(release_type) == str:
            release_type: int = [
                i for i in mappings_release if mappings_release[i] == release_type][0]

        if type(importance[0]) == str:
            importance: List[int] = [[
                j for j in mappings_artist_importance if mappings_artist_importance[j] == i][0] for i in importance]
        try:
            if not kwargs:
                remaster_year = year
                torrent = TorrentUpload(category, artists, importance, title, year, release_type, format,
                                        bitrate, media, tags, image, album_desc, torrent_desc, remaster_year)
            elif kwargs["remaster_year"] is None:
                remaster_year = year
                torrent = TorrentUpload(category, artists, importance, title, year, release_type, format,
                                        bitrate, media, tags, image, album_desc, torrent_desc, remaster_year, **kwargs)
            else:
                torrent = TorrentUpload(category, artists, importance, title, year, release_type, format,
                                        bitrate, media, tags, image, album_desc, torrent_desc, **kwargs)
            return torrent
        except KeyError as e:
            return e

    def upload_torrent(self, filepath: str, filename: str, torrent: TorrentUpload):
        file = {
            "file_input": (filename, open(os.path.join(filepath, filename), 'rb'), 'application/x-bittorrent')
        }
        arguments = asdict(torrent)
        r = self.sess.session.post(self.url, data=arguments, files=file)
        return r.resp

    # TODO report for LMA/LWA
    def report(self):
        pass

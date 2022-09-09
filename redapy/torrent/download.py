from redapy.base import BaseAuth, TorrentDownload, urls, Failure
from typing import Optional, Union
import os


class Download():
    def __init__(self) -> None:
        self.sess = BaseAuth()

    def get_torrent_data(self, id: int) -> TorrentDownload:
        self.url_details: str = urls["base_url"] + urls["torrent_details"]

        r = self.sess.session.get(self.url_details + f'id={id}')
        resp_json = r.json()

        artists = [i["name"]
                   for i in resp_json["response"]["group"]["musicInfo"]["artists"]]
        name = resp_json["response"]["group"]["name"]
        media = resp_json["response"]["torrent"]["media"]
        format = resp_json["response"]["torrent"]["format"]
        encoding = resp_json["response"]["torrent"]["encoding"]
        torrent = TorrentDownload(artists, name, id, media, format, encoding)
        return torrent

    def download_torrent(self, id: int, target_dir: Optional[str] = os.getcwd(), token: Optional[Union[int, bool]] = 0):
        self.url_dl: str = urls["base_url"] + urls["torrent_dl"]

        if type(token) == bool:
            token = int(token)

        r = self.sess.session.get(
            self.url_dl + f'id={id}&usetoken={token}', stream=True)
        r_cont_b = bytes(r.content)

        torrent = self.get_torrent_data(id)
        artists = ', '.join(torrent.artists)
        filename = f'{artists} - {torrent.name} [{torrent.media} {torrent.format} {torrent.encoding}].torrent'
        filepath: str = os.path.join(target_dir, filename)

        try:
            with open(filepath, 'wb') as f:
                f.write(r_cont_b)
        except IOError:
            return Failure(f'Cannot open file for writing {filename}')

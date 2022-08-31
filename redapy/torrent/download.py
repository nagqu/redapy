from redapy.base import BaseAuth, TorrentDownload, urls
from typing import Optional


class Download():
    def __init__(self) -> None:
        self.sess = BaseAuth()

    def get_torrent_data(self, id: int) -> TorrentDownload:
        self.url_details: str = urls["base_url"] + urls["torrent_details"]
        r = self.sess.session.get(self.url_details + f'id={id}')
        resp_json = r.json()

        torrent = TorrentDownload()
        torrent.artists = [i["name"]
                           for i in resp_json["response"]["group"]["musicInfo"]["artists"]]
        torrent.name = resp_json["response"]["group"]["name"]
        torrent.id = id
        torrent.media = resp_json["response"]["torrent"]["media"]
        torrent.format = resp_json["response"]["torrent"]["format"]
        torrent.encoding = resp_json["response"]["torrent"]["encoding"]
        return torrent

# TODO finish try/except
    def download_torrent(self, id: int, token: Optional[int] = 0):
        self.url_dl: str = urls["base_url"] + urls["torrent_dl"]
        r = self.sess.session.get(
            self.url_dl + f'id={id}&usetoken={token}', stream=True)
        r_cont_b = bytes(r.content)

        torrent = self.get_torrent_data(id)
        artists = ', '.join(torrent.artists)
        filename = f'{artists} - {torrent.name} [{torrent.media} {torrent.format} {torrent.encoding}].torrent'

        try:
            with open(filename, 'wb') as f:
                f.write(r_cont_b)
        except Exception as e:
            print(f'Failed to write a file\n {e}')

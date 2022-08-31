from dataclasses import asdict
import os
from redapy.base import BaseAuth, Torrent, urls
from typing import List
from base64 import b64encode


# No Log support for now

class Upload():
    def __init__(self):
        self.sess = BaseAuth()
        self.url: str = urls["base_url"] + urls["torrent_up"]

    def upload_torrent(self, filepath: str, filename: str, torrent: Torrent):
        file = {
            "file_input": (filename, open(os.path.join(filepath, filename), 'rb'), 'application/x-bittorrent')
        }
        arguments = asdict(torrent)
        r = self.sess.session.post(self.url, data=arguments, files=file)

    # TODO report for LMA/LWA
    def report(self):
        pass

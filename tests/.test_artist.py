from typing import List
from redapy.base import *
from redapy.artist import Artist
from redapy.torrent.upload import Upload

# Due to new torrents being uploaded tests work at the time of writing


class TestArtist():
    def __init__(self) -> None:
        self.artist: Artist = Artist()

    def test_get_artists_torrents(self):
        rysy_torrent_ids: List[int] = self.artist.get_artist_torrent_ids(
            487223)
        assert rysy_torrent_ids == [3347868, 2693034, 3211899, 1595375]

    def test_get_artists_torrents_format(self):
        swies_torrent_ids: List[int] = self.artist.get_artist_torrent_ids(
            274601, "MP3")
        assert swies_torrent_ids == [
            2279520, 2103591, 2267994, 3181160, 3181158, 3176387]

    def test_get_artists_torrents_format_enc(self):
        kavari_torrent_ids: List[int] = self.artist.get_artist_torrent_ids(
            1094352, "FLAC", "24bit Lossless")

        assert kavari_torrent_ids == [3525182, 3525361, 3751478]

    def test_requests(self):
        umru_req: List[Request] = self.artist.get_request(539814)
        assert umru_req[0].id == 98557
        assert umru_req[0].category == "Album"
        assert umru_req[0].title == "Pop 2"

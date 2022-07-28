from base import BaseAuth, URLs
import json


class Artist():
    def __init__(self):
        urls = URLs()
        self.url: str = urls.get_artist()
        self.sess = BaseAuth()

    def artist_by_id(self, id: int):
        r = self.sess.session.get(self.url + f'id={id}')
        resp_json = r.json()
        artist_name: str = resp_json["response"]["name"]
        vanity_house: bool = resp_json["response"]["vanityHouse"]
        tags: dict = resp_json["response"]["tags"]

        return resp_json

    # to implement further
    # def artist_by_name(self, name: str):
    #     name = name.replace(' ', '+')
    #     r = self.sess.session.get(self.url + f'artistname={name}')
    #     return r.content

    def get_artist_torrent_ids(self, id: int, format: str = "", encoding: str = ""):
        artist_page: dict = self.artist_by_id(id)
        torrentgroups = artist_page["response"]["torrentgroup"]
        torrent_ids = []
        # it somehow works but is inefficient af
        for i in torrentgroups:
            i = dict(i)
            if format != "":
                if encoding != "":
                    for j in i["torrent"]:
                        if j["format"] == format and j["encoding"] == encoding:
                            torrent_ids.append(j["id"])
                else:
                    for j in i["torrent"]:
                        if j["format"] == format:
                            torrent_ids.append(j["id"])
            else:
                for j in i["torrent"]:
                    torrent_ids.append(j["id"])
        return torrent_ids

    def get_requests(self, id: int):
        pass

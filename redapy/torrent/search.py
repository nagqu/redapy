from typing import List, Optional
from redapy.base import TorrentGroup, Torrent, urls, BaseAuth


class Search():
    def __init__(self):
        self.sess = BaseAuth()
        self.url = urls["base_url"] + urls["torrent_search"]

    # TODO searchstr can be none // all but page kwargs, dejsonify
    # -> List[TorrentGroup]:
    def search_torrent(self, search_str: str, page: Optional[int] = 1, **kwargs) -> List[TorrentGroup]:
        params = {
            "searchstr": search_str,
            "page": page,
            **kwargs
        }
        response = self.sess.session.get(self.url, params=params)
        r_json = response.json()
        results = r_json["response"]["results"]

        groups: List[TorrentGroup] = []

        for i in results:
            torrents = i["torrents"]
            torr_list: List[Torrent] = []
            for j in torrents:
                torrent = Torrent(
                    j["torrentId"],
                    [x for x in j["artists"]],  # needs proper impl
                    j["remastered"],
                    j["remasterYear"],
                    j["remasterCatalogueNumber"],
                    j["remasterTitle"],
                    j["media"],
                    j["encoding"],
                    j["format"],
                    j["hasLog"],
                    j["logScore"],
                    j["hasCue"],
                    j["scene"],
                    j["vanityHouse"],
                    j["fileCount"],
                    j["time"],
                    j["size"],
                    j["snatches"],
                    j["seeders"],
                    j["leechers"],
                    j["isFreeleech"],
                    j["isFreeload"],
                    j["isPersonalFreeleech"],
                    j["canUseToken"],
                    j["hasSnatched"]

                )
                torr_list.append(torrent)
            group = TorrentGroup(
                i["groupId"],
                i["groupName"],
                i["artist"],
                [x for x in i["tags"]],
                bool(i["bookmarked"]),
                bool(i["vanityHouse"]),
                i["groupYear"],
                i["releaseType"],
                torr_list
            )
            groups.append(group)

        return groups

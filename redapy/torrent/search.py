from typing import List, Optional
from redapy.base import TorrentGroup, urls, BaseAuth


class Search():
    def __init__(self):
        self.sess = BaseAuth()
        self.url = urls["base_url"] + urls["torrent_search"]

    # TODO searchstr can be none // all but page kwargs, dejsonify
    def search_torrent(self, search_str: str, page: Optional[int] = 1, **kwargs) -> List[TorrentGroup]:
        params = {
            "searchstr": search_str,
            "page": page,
            **kwargs
        }
        response = self.sess.session.get(self.url, params=params)

        return response.json()


s = Search()
print(s.search_torrent("", tags="reggaeton"))

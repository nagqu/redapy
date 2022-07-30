from dataclasses import dataclass
import requests
from dotenv import load_dotenv
import os

mappings: dict[int, str] = {
    1: "Album",
    3: "Soundtrack",
    5: "EP",
    6: "Anthology",
    7: "Compilation",
    9: "Single",
    11: "Live album",
    13: "Remix",
    14: "Bootleg",
    15: "Interview",
    16: "Mixtape",
    17: "Demo",
    18: "Concert Recording",
    19: "DJ Mix",
    21: "Unknown",
    1021: "Produced By",
    1022: "Composition",
    1023: "Remixed By",
    1024: "Guest Appearance"
}


@dataclass()
class Request():
    id: int
    title: str
    category: int
    bounty: int


class BaseAuth():
    def __init__(self):
        load_dotenv()
        self.session = requests.Session()
        self.session.headers.update({"Authorization": os.getenv('APIKEY')})


class URLs():
    def __init__(self):
        self.base_url: str = "https://redacted.ch/"
        self.index: str = "ajax.php?action=index"
        self.user_profile: str = "ajax.php?action=user"
        self.inbox: str = "ajax.php?action=inbox"
        self.conversation: str = "ajax.php?action=inbox&type=viewconv"
        self.send_pm: str = "ajax.php?action=send_pm"
        self.top10: str = "ajax.php?action=top10"
        self.user_search: str = "ajax.php?action=usersearch"
        self.bookmarks: str = "ajax.php?action=bookmarks&type="
        self.subs: str = "ajax.php?action=subscriptions"
        self.forum_category: str = "ajax.php?action=forum&type=main"
        self.forum_view: str = "ajax.php?action=forum&type=main"
        self.thread_view: str = "ajax.php?action=forum&type=viewthread&threadid="
        self.artist: str = "ajax.php?action=artist&"
        self.torrent_search: str = "ajax.php?action=browse&"

    def get_base_url(self) -> str:
        return self.base_url

    def get_index(self) -> str:
        return self.base_url + self.index

    def get_user_profile(self) -> str:
        return self.base_url + self.user_profile

    def get_inbox(self) -> str:
        return self.base_url + self.inbox

    def get_conversation(self) -> str:
        return self.base_url + self.conversation

    def get_send_pm(self) -> str:
        return self.base_url + self.send_pm

    def get_top10(self) -> str:
        return self.base_url + self.top10

    def get_user_search(self) -> str:
        return self.base_url + self.user_search

    def get_bookmarks(self) -> str:
        return self.base_url + self.bookmarks

    def get_subs(self) -> str:
        return self.base_url + self.subs

    def get_forum_category(self) -> str:
        return self.base_url + self.forum_category

    def get_forum_view(self) -> str:
        return self.base_url + self.forum_view

    def get_thread_view(self) -> str:
        return self.base_url + self.thread_view

    def get_artist(self) -> str:
        return self.base_url + self.artist

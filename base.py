from dataclasses import dataclass
import requests
from dotenv import dotenv_values, load_dotenv
import os


class BaseAuth():
    def __init__(self):
        # self.api_key = dotenv_values()
        load_dotenv()
        self.session = requests.Session()
        self.session.headers.update({"Authorization": os.getenv('APIKEY')})


class URLs():
    def __init__(self):
        self.base_url = "https://redacted.ch/"
        self.index = "ajax.php?action=index"
        self.user_profile = "ajax.php?action=user"
        self.inbox = "ajax.php?action=inbox"
        self.conversation = "ajax.php?action=inbox&type=viewconv"
        self.send_pm = "ajax.php?action=send_pm"
        self.top10 = "ajax.php?action=top10"
        self.user_search = "ajax.php?action=usersearch"
        self.bookmarks = "ajax.php?action=bookmarks&type="
        self.subs = "ajax.php?action=subscriptions"
        self.forum_category = "ajax.php?action=forum&type=main"
        self.forum_view = "ajax.php?action=forum&type=main"
        self.thread_view = "ajax.php?action=forum&type=viewthread&threadid="
        self.artist = "ajax.php?action=artist&id="
        self.torrent_search = "ajax.php?action=browse&"

    def get_base_url(self):
        return self.base_url

    def get_index(self):
        return self.base_url + self.index

    def get_user_profile(self):
        return self.base_url + self.user_profile

    def get_inbox(self):
        return self.base_url + self.inbox

    def get_conversation(self):
        return self.base_url + self.conversation

    def get_send_pm(self):
        return self.base_url + self.send_pm

    def get_top10(self):
        return self.base_url + self.top10

    def get_user_search(self):
        return self.base_url + self.user_search

    def get_bookmarks(self):
        return self.base_url + self.bookmarks

    def get_subs(self):
        return self.base_url + self.subs

    def get_forum_category(self):
        return self.base_url + self.forum_category

    def get_forum_view(self):
        return self.base_url + self.forum_view

    def get_thread_view(self):
        return self.base_url + self.thread_view

    def get_artist(self):
        return self.base_url + self.artsit


# u = URLs()
# print(u.get_index())

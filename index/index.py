from base import BaseAuth, URLs
import requests


class Index():
    def __init__(self):
        urls = URLs()
        self.url: str = urls.get_index()

    def get_index(self):
        s = BaseAuth()
        r = s.session.get(self.url)
        print(r.content)


index = Index()
print(index.get_index())

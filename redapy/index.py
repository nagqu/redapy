from base import BaseAuth, urls


class Index():
    def __init__(self):
        self.url: str = urls["base_url"] + urls["index"]

    def get_index(self):
        s = BaseAuth()
        r = s.session.get(self.url)
        print(r.content)

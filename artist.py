from lib2to3.pytree import Base
from yarl import URL
from base import BaseAuth, URLs

class Artist():
    def __init__(self):
        urls = URLs()
        self.url = urls.get_artist()
        self.session = BaseAuth()
        
    def artist_by_id(self, id):
        r = self.session.get(self.url + f'id={id}')
        return r.content
    
    def artist_by_name(self, name):
        r = self.session.get(self.url + f'artistname={name}')
        return r.content
    
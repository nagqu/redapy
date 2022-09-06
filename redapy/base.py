from dataclasses import dataclass
import requests
from dotenv import load_dotenv
import os
from typing import List, Dict, Optional

mappings_release: Dict[int, str] = {
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
    21: "Unknown"
}

mappings_categories: Dict[int, str] = {
    0: "Music",
    1: "Applications",
    2: "E-Books",
    3: "Audiobooks",
    4: "E-Learning Videos",
    5: "Comedy",
    6: "Comics"
}

mappings_artist: Dict[int, str] = {
    1021: "Produced By",
    1022: "Composition",
    1023: "Remixed By",
    1024: "Guest Appearance"
}

mappings_artist_importance: Dict[int, str] = {
    1: "Main",
    2: "Guest",
    3: "Composer",
    4: "Conductor",
    5: "DJ / Compiler",
    6: "Remixer",
    7: "Producer",
}


@dataclass
class Request():
    id: int
    title: str
    category: int  # Album, EP ...
    bounty: int  # in bytes


@dataclass
class TorrentDownload():
    artists: List[str]
    name: str
    id: int
    media: str
    format: str
    encoding: str


@dataclass
class TorrentUpload():
    category: int
    artists: List[str]
    importance: List[int]
    title: str
    year: int
    releasetype: int
    format: str
    bitrate: str
    media: str
    tags: str
    image: str
    album_desc: str
    desc: str
    remaster_year: Optional[int] = None  # if not provided = year
    unknown: Optional[bool] = None
    groupid: Optional[int] = None
    requestid: Optional[int] = None
    release_desc: Optional[str] = None
    vanity_house: bool = None
    other_bitrate: Optional[str] = None
    vbr: Optional[bool] = None
    remaster_title: Optional[str] = None
    remaster_record_label: Optional[str] = None
    remaster_catalogue_number: Optional[str] = None
    scene: Optional[bool] = None


@dataclass
class BookmarkedTorrent():
    group_id: int


class BaseAuth():
    def __init__(self):
        load_dotenv()
        self.session = requests.Session()
        self.session.headers.update({"Authorization": os.getenv('APIKEY')})


urls: Dict[str, str] = {
    "base_url": "https://redacted.ch/",
    "index": "ajax.php?action=index",
    "user_profile": "ajax.php?action=user",
    "inbox": "ajax.php?action=inbox",
    "conversation": "ajax.php?action=inbox&type=viewconv",
    "send_pm": "ajax.php?action=send_pm",
    "top10": "ajax.php?action=top10",
    "user_search": "ajax.php?action=usersearch",
    "bookmarks": "ajax.php?action=bookmarks&type=",
    "subs": "ajax.php?action=subscriptions",
    "forum_category": "ajax.php?action=forum&type=main",
    "forum_view": "ajax.php?action=forum&type=main",
    "thread_view": "ajax.php?action=forum&type=viewthread&threadid=",
    "artist": "ajax.php?action=artist&",
    "torrent_search": "ajax.php?action=browse&",
    "torrent_dl": "ajax.php?action=download&",
    "torrent_details": "ajax.php?action=torrent&",
    "torrent_up": "ajax.php?action=upload"
}

class Failure(Exception):
    pass
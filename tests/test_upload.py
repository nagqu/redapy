from redapy.torrent.upload import Upload


class TestUpload():
    def test_preapre_torrent(self):
        upload = Upload()
        torrent = upload.prepare_torrent(
            "Music",
            ["DJ AK BR", "DJ Darge"],
            ["Main", "Main"],
            "Melodia Alucinógena",
            2022,
            "Single",
            "MP3",
            320,
            "WEB",
            "reggaeton",
            "https://ptpimg.me/91lf78.jpg",
            "[size=4][b]Tracklist[/b][/size]\n[b]1.[/b] Melodia Alucinógena[i](03: 03)[/i]\n[b]Total length: [/b] 03: 03\nMore information: [url]https: // www.deezer.com/en/album/334123947[/url]",
            ""
        )
        assert torrent.category == 0
        assert torrent.importance == [1, 1]
        assert torrent.releasetype == 9
        assert torrent.remaster_year == 2022

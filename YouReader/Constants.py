
class prefix:
    YOUTUBE = "https://www.youtube.com/"
    VIDEO = "watch?v="
    PLAYLIST = "playlist?list="

    def __init__(self):
        pass

class regex:
    INDEX = r"[\d]+\n"
    TIME = r"(\d\d:\d\d:\d\d,\d\d\d \-\-\> \d\d:\d\d:\d\d,\d\d\d\s)|(\d\d:\d\d:\d\d\d\d\d)"
    PUNCT = r"[?,.!:\%;\]\[\"\(\)\^\_\/\{\}\>\<\*\#]|\-\-|"
    ACTION = r"\[[a-zA-Z]+\]"
    SPEAKER = r"[a-zA-Z]+:\s"
    ID = r"[a-zA-Z0-9_-]{11}"

    def __init__(self):
        pass


class path:
    LINKS = "data/links.csv"
    EXAMPLE= "data/example.csv"
    SAVE = "data/save.json"

    def __init__(self):
        pass

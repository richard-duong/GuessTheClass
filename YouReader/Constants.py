

class prefix:
    YOUTUBE = "https://www.youtube.com/"
    VIDEO = "watch?v="
    PLAYLIST = "playlist?list="

    def __init__(self):
        pass


class regex:
    INDEX = r"[\d]+\n"
    TIME = r"\d\d:\d\d:\d\d,\d\d\d \-\-\> \d\d:\d\d:\d\d,\d\d\d\n"
    PUNCT = r"[?,.]"
    ACTION = r"\[[a-zA-Z]+\]"
    SPEAKER = r"[a-zA-Z]+:"
    IDENTIFIER = r"watch?v=([a-zA-Z0-9]+)"

    def __init__(self):
        pass


class path:
    LINKS = "../data/links.csv"
    EXAMPLE= "../data/example.csv"
    SAVE = "../data/save.json"

    def __init__(self):
        pass

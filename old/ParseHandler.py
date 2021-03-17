import re
from Constants import regex

class ParseHandler: 
    def __init__(self):
        pass

    def parse_youtube(self, text: str) -> str:
        reg = regex.EXTENDED_TIME + "|" + regex.PUNCT + "|"
        return re.sub(reg, " ", text)

    def parse_yuja(self, text: str) ->str:
        reg = regex.TIME + "|" + regex.PUNCT
        return re.sub(reg, " ", text)

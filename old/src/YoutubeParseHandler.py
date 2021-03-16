import re
import YoutubeRegex


class YoutubeParseHandler:
    def __init__(self):
        self.__wordsList = []

    def __parseFile(self, transcript):
        with open(transcript, "r") as inFile:
            text = inFile.read()
        text = re.sub(YoutubeRegex.BASIC_FILTER + "|" + YoutubeRegex.ACTION + "|"
                      + YoutubeRegex.ARROW + "|" + YoutubeRegex.DICTATE_SPEAKER, " ", text)
        self.__wordsList = text.split()

    def __writeFile(self, filteredFile):
        with open(filteredFile, "w") as outFile:
            for word in self.__wordsList:
                outFile.write("{}\n".format(word.lower()))

    def parse(self, transcript, filteredFile):
        self.__parseFile(transcript)
        self.__writeFile(filteredFile)

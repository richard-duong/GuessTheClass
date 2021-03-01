import re
import regex

class ParseHandler: 
    def __init__(self):
        self.__wordsList = []	

    def __parseFile(self, srcFile):
        with open(srcFile, "r") as inFile:
            text = inFile.read()
        text = re.sub(regex.TIME + "|" + regex.PUNCT, " ", text) 
        self.__wordsList = text.split()
            
    def __writeFile(self, destFile):
        with open(destFile, "w") as outFile:
            for word in self.__wordsList:
                outFile.write("{}\n".format(word.lower()))

    def parse(self, srcFile, destFile):	
        self.__parseFile(srcFile)
        self.__writeFile(destFile)	

import re

def parse(srcFile, destFile):

    # open file for reading
    with open(srcFile, "r") as inFile:
        text = inFile.read()

    # substitute timestamps & punctuation with spaces
    text = re.sub(r'(\d\d:\d\d)|[.?!,]', ' ', text)

    # generate list of words
    words = text.split()

    # open file for writing
    with open(destFile, "w") as outFile:
        for word in words:
            outFile.write("{}\n".format(word))

src = "../resources/Text/CS/cs105_011121_uncleaned.txt"
dest = "../resources/Text/CS/cs105_011121_cleaned.txt"

parse(src, dest)

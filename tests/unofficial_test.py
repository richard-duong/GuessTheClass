import sys
import re

from pytube import YouTube
from YouReader.Reader import Reader
from YouReader.Constants import regex

def english_video_links():
    '''Returns list of testable video links'''
    video_links = []
    video_links.append("https://www.youtube.com/watch?v=7Nbv3reNErw")
    video_links.append("https://www.youtube.com/watch?v=_jqEqmc35yk")
    video_links.append("https://www.youtube.com/watch?v=TQTlCHxyuu8")
    video_links.append("https://www.youtube.com/watch?v=om3n2ni8luE")
    video_links.append("https://www.youtube.com/watch?v=iH08rrt38m8")
    return video_links

def english_video_ids():
    '''Returns matching list of unique id to english_video_links'''
    video_ids = []
    video_ids.append("7Nbv3reNErw")
    video_ids.append("_jqEqmc35yk")
    video_ids.append("TQTlCHxyuu8")
    video_ids.append("om3n2ni8luE")
    video_ids.append("iH08rrt38m8")
    return video_ids

def raw_caption():
    with open("tests/data/raw_caption.srt", "r") as inFile:
        text = inFile.read()
    return text

def clean_caption():
    with open("tests/data/clean_caption.srt", "r") as inFile:
        text = inFile.read()
    return text

# compare unique_id
def test1():
    reader = Reader()
    links = english_video_links()
    vids = english_video_ids()

    for link, vid in zip(links, vids):
        print(reader.__get_unique_id__(link))
        print(vid)
        print()


# compares clean vs raw captions
def test2():
    reader = Reader()
    raw = raw_caption()
    clean = clean_caption()

    print(raw)
    print("==========================") 
    print(reader.__get_clean_caption__(raw))
    print("==========================")
    print(clean)


def test3():
    reader = Reader()
    raw = raw_caption()
    clean = clean_caption()

    text1 = re.sub(regex.TIME, "", raw)
    print("Without timestamps")
    print("==================")
    print(text1)
    

if __name__ == "__main__" and len(sys.argv) == 2:
    if sys.argv[1] == "1":
        test1()

    elif sys.argv[1] == "2":
        test2()

    elif sys.argv[1] == "3":
        test3()




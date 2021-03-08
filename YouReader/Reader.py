# Python Libraries
import json
import pandas as pd

# External Libraries
from pytube import YouTube

# Custom Libraries
from Constants import prefix
from Constants import regex
from Constants import path



class Reader:

    def __init__(self) -> None:
        pass

    def download_csv_captions(self, raw_path: str = path.RAW, links: str = path.LINKS) -> list: 
        
        with open(path.COLLECTION, "r") as data:
            collection = json.load(data)

        df = pd.read_csv(links)
       
        # start reading in link by link
        # identify link as video, playlist, or neither
        # generate a full list of video links

        # after identifying video links, run links through collection to see if
        # we have already parsed that link

        # water down to links that have not been inserted
        # insert each video by unique video id and preserve:
        #       -> subject
        #       -> notes
        #       -> link


    def 

    
    


    
 

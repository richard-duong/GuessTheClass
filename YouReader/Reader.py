# Python Libraries
import csv
import json
import pandas as pd
import re

# External Libraries
from pytube import YouTube
from pytube import Playlist

# Custom Libraries
from YouReader.Constants import prefix
from YouReader.Constants import regex
from YouReader.Constants import path
from YouReader.ParseHandler import Parser



class Reader:

    def __init__(self) -> None:
        self.data = {}
        pass


    # returns youtube's unique id for video
    def __get_unique_id__(self, link: str) -> str:
        unique_id = re.search(regex.IDENTIFIER, link)
        if unique_id:
            return unique_id.group(1) 
        else:
            return ""


    # returns the unique youtube link
    def __get_unique_link__(self, unique_id: str) -> str:
        if unique_id != "":
            return prefix.YOUTUBE + prefix.VIDEO + unique_id

    
    # returns video links from playlist
    def __get_playlist_links__(self, link: str) -> list:
        pass
                

    # retrieves caption from unique youtube id
    def __get_raw_caption__(self, unique_link: str, code: str = "en") -> str:
        source = YouTube(unique_link)

        # custom user code captions
        if code != "en" and code in source.captions:
            raw_caption = source.captions[code].generate_srt_captions()

        # default english captions
        if code == "en" and "en" in source.captions:
            raw_caption = source.captions["en"].generate_srt_captions()

        # default auto generated english
        elif code == "en" and "a.en" in source.captions:
            raw_caption = source.captions["a.en"].generate_srt_captions()

        # no matching code
        else:
            raw_caption = ""

        return raw_caption



    # cleans raw caption
    def __get_clean_caption__(self, caption: str = "") -> str:
        reg = regex.INDEX + "|" + regex.TIME + "|" regex.ACTION + "|" regex.PUNCT + "|" regex.SPEAKER
        caption = re.sub(reg, "", caption)
        caption = caption.lower()
        return caption
        

    # generates caption entry
    def __generate_entry__(self, link: str, subject: str, notes: str) -> dict:
        entry = {}
        unique_id = self.__get_unique_id__(link)
        unique_link = self.__get_unique_link__(unique_id)
        raw = self.__get_raw_caption__(self, unique_link)
        clean = self.__get_clean_caption__(self, raw)
        if raw != "":
            entry["link"] = unique_link
            entry["subject"] = subject
            entry["notes"] = notes
            entry["raw"] = raw
            entry["clean"] = clean
        return entry
                

    # loads captions from save file
    def load_captions(self, save_file: str = path.SAVE) -> int:
        with open(save_file, "r") as inFile:
           self.data = json.load(inFile)
        return len(self.data)


    # saves captions to save file
    def save_captions(self, save_file: str = path.SAVE) -> int:
        with open(save_file, "w") as outFile:
            json.dump(self.data, outFile)
        return len(self.data)


    # downloads all captions from csv file and returns dictionary
    def download_csv_captions(self, csv_file: str = path.LINKS) -> dict: 
        
        with open(csv_file) as inFile:
            data = csv.DictReader(inFile)

        for row in data:

            # if user inserted video
            if prefix.VIDEO in row['link']:
                unique_id = self.__get_unique_id__(link) 

                # check if video is already in dataset
                if unique_id not in self.data:
                    entry = self.__generate_entry__(row['link'], row['subject'], row['notes'])  
                    self.data[unique_id] = entry
                
            # if user inserted playlist
            elif prefix.PLAYLIST in row['link']:
                video_links = Playlist(row['link'])

                # iterate through all video links
                for link in video_links:
                    unique_id = self.__get_unique_id__(link)

                    # check if video is already in dataset
                    if unique_id not in self.data:
                        entry = self.__generate_entry__(link, row['subject'], row['notes'])
                        self.data[unique_id] = entry

            # not a video or playlist
            else:
                raise ValueError('Please provide a valid video or playlist link')

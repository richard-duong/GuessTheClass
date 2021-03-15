# Python Libraries
import csv
import json
import pandas as pd
import re
import time

# External Libraries
from pytube import YouTube
from pytube import Playlist

# Custom Libraries
from YouReader.Constants import prefix
from YouReader.Constants import regex
from YouReader.Constants import path


# notes to come back to:
# - add a verbose flag for download_csv_captions()
# - reformat seconds in the time print for download_csv_captions()


class Reader:

    def __init__(self, code: str = "en") -> None:
        self.data = dict()
        self.code = code
        self.csv_count = 0
        pass


    # returns youtube's unique id for video
    def __get_unique_id__(self, link: str) -> str:
        unique_id = re.search(regex.ID, link)
        if unique_id:
            return unique_id.group(0)
        else:
            return ""


    # returns the unique youtube link
    def __get_unique_link__(self, unique_id: str) -> str:
        if unique_id != "":
            return prefix.YOUTUBE + prefix.VIDEO + unique_id
                

    # retrieves caption from unique youtube id
    def __get_raw_caption__(self, unique_link: str) -> str:
        source = YouTube(unique_link)
        code = self.code

        # custom user code captions
        if code != "en" and code in source.captions:
            raw_caption = source.captions[code].generate_srt_captions()

        # default english captions
        elif code == "en" and "en" in source.captions:
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
        reg = regex.INDEX + "|" + regex.TIME + "|" + regex.ACTION + "|" + regex.PUNCT + "|" + regex.SPEAKER
        caption = re.sub(reg, "", caption)
        caption = caption.lower()
        return caption

    # return true if link is a playlist
    def __is_playlist__(self, link: str = "") -> bool:
        if prefix.PLAYLIST in link:
            return True
        return False

    # return true if link is a video
    def __is_video__(self, link: str = "") -> bool:
        if prefix.VIDEO in link:
            return True
        return False 

    # generates caption entry
    def __generate_entry__(self, link: str, subject: str, notes: str) -> dict:
        entry = {}
        unique_id = self.__get_unique_id__(link)
        unique_link = self.__get_unique_link__(unique_id)
        raw = self.__get_raw_caption__(unique_link)
        clean = self.__get_clean_caption__(raw)
        entry["link"] = unique_link
        entry["subject"] = subject
        entry["notes"] = notes
        entry["raw"] = raw
        entry["clean"] = clean
        return entry


    # generates entry for video data
    def __download_video__(self, row: dict) -> int:
        video_count = 0
        unique_id = self.__get_unique_id__(row["link"])
        if unique_id not in self.data:
            self.data[unique_id] = self.__generate_entry__(row)
            video_count += 1 
        return video_count
            

    # generates entry for playlist data
    def __download_playlist__(self, row: dict, threads: int = 1) -> int:
        video_counts = []
        video_entries = []
        video_links = Playlist(row["link"])

        for link in video_links:
           entry = row.copy()
           entry["link"] = link
           video_entries.append(entry)

        with ThreadPool(threads) as pool:
            video_counts = pool.map(self.__download_video__, video_entries)

        return sum(video_counts)
                

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

    # retrieves list of keys (can filter by subject)
    def get_list_keys(self, subject: str = "") -> list: 
        keys_list = list(self.data.keys())
        if subject != "":
            keys_list = [key for key in keys_list if self.data[key]["subject"] == subject if self.data[key]["raw"] != ""]
        else:
            keys_list = [key for key in keys_list if self.data[key]["raw"] != ""]
        return keys_list

    # retrieves list of links (can filter by subject)
    def get_list_link(self, subject: str = "") -> list: 
        keys_list = self.get_list_keys(subject)
        link_list = [self.data[key]["link"] for key in keys_list]
        return link_list

    # retrieves list of subjects (can filter by subject)
    def get_list_subject(self, subject: str = "") -> list:
        keys_list = self.get_list_keys(subject)
        subject_list = [self.data[key]["subject"] for key in keys_list]
        return subject_list

    # retrieves list of notes (can filter by subject)
    def get_list_notes(self, subject: str = "") -> list: 
        keys_list = self.get_list_keys(subject)
        notes_list = [self.data[key]["notes"] for key in keys_list]
        return notes_list

    # retrieves list of raw captions (can filter by subject)
    def get_list_raw_captions(self, subject: str = "") -> list: 
        keys_list = self.get_list_keys(subject)
        raw_list = [self.data[key]["raw"] for key in keys_list]
        return raw_list

    # retrieves list of clean captions (can filter by subject)
    def get_list_clean_captions(self, subject: str = "") ->list: 
        keys_list = self.get_list_keys(subject)
        clean_list = [self.data[key]["clean"] for key in keys_list]
        return clean_list

    # retrieves list of clean captions
    def get_list_clean(self) -> list:
        return [data[key]["clean"] for key in data if data[key]["raw"] != ""]
    
    # retrieves list of raw captions
    def get_list_raw(self) -> list:
        return [data[key]["raw"] for key in data if data[key]["raw"] != ""]

    # retrieves list of links
    def get_list_link(self) -> list:
        return [data[key]["link"] for key in data if data[key]["raw"] != ""]

    # retrieves list of notes
    def get_list_note(self) -> list:
        return [data[key]["notes"] for key in data if data[key]["raw"] != ""]

    # converts data to a dataframe with keys as columns, indexed by id
    def to_dataframe(self) -> pd.DataFrame:
        df = pd.DataFrame(self.data)
        df_trans = df.transpose()
        df_filter = df_trans[df_trans["raw"] != ""]
        return df_filter

    # erases keys/data for videos that do not have the desired transcripts
    def erase_unused(self) -> list:
        keys_set = set(self.get_list_keys())
        new_data = {key:val for key, val in self.data.items() if key in keys_set}        

    # downloads all captions from csv file and returns dictionary
    def download_csv_captions(self, csv_file: str = path.LINKS, subject: str = "", code: str = "") -> None:  
        count = 0 
        video_count = 0
        start_time = time.time()
        
        if str != "":
            self.code = code
    
        with open(csv_file) as inFile:
            data = csv.DictReader(inFile)

            for row in data:

                count += 1
                video_time = time.time()
                print("Downloading row number", count, ":\t", row["subject"], " - ", row["notes"])

                # if user inserted video
                if prefix.VIDEO in row['link'] and (row["subject"] == "" or row["subject"] == subject):
                    unique_id = self.__get_unique_id__(row['link']) 

                    # check if video is already in dataset
                    if unique_id not in self.data:
                        video_count = 1
                        entry = self.__generate_entry__(row['link'], row['subject'], row['notes'])  
                        self.data[unique_id] = entry
                    
                # if user inserted playlist
                elif prefix.PLAYLIST in row['link'] and (row["subject"] == "" or row["subject"] == subject):
                    video_links = Playlist(row['link'])

                    # iterate through all video links
                    for link in video_links:
                        video_count += 1
                        unique_id = self.__get_unique_id__(link)

                        # check if video is already in dataset
                        if unique_id not in self.data:
                            entry = self.__generate_entry__(link, row['subject'], row['notes'])
                            self.data[unique_id] = entry

                # not a video or playlist
                else:
                    raise ValueError('Please provide a valid video or playlist link')

                print("Videos downloaded: ", video_count, " ----- Time taken: ", time.time() - video_time, "seconds ----- Elapsed time: ", time.time() - start_time, " seconds\n")


    # downloads all captions from csv
    def download_csv_captions_2(self, csv_file: str = path.Links, code: str = "en", threads: int = 1, verbose: bool = False) -> None:
        start_time = time.time()
        with open(csv_file) as infile:
            csv_rows = csv.DictReader(inFile)

            for row in csv_rows: 

                row_time = time.time()

                if verbose == True:
                    print("Downloading row number", count, ":\t", row["subject"], "---", row["subject name"], "---", row["topic"], "---", row["notes"])

                if self.__is_video__(row["link"]) == True:
                    video_count = self.__download_video__(row, verbose, threads)

                elif self.__is_playlist__(row["link"]) == True:
                    video_count = self.__download_playlist__(row, verbose, threads)

                else:
                    raise ValueError('Please provide a valid video or playlist link')

                if verbose == True:
                    print("Videos downloaded:", video_count, " ----- Time taken: ", time.time() - row_time, "seconds ----- Elapsed time: ", time.time() - start_time, " seconds\n")





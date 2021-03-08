from Constants import prefix
from Constants import regex
from pytube import Playlist


link = input("Enter a link: ")

if prefix.video in link:
    print("This is a video")

elif prefix.playlist in link:
    print("This is a playlist")

else:
    print("This is neither")

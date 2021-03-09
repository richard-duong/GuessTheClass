# Guess The Class
A CS105 Project that classifies and characterizes class lectures based on frequency of words.<br>
Project developed by Shreya Balaji, Benson Wan, and Richard Duong<br>
[Link to the Github Repository Here](https://github.com/richard-duong/ClassIdentifier)<br><br>

----------------------
<a name="overview"/>

Overview
========




------------------------------
<a name="table-of-contents"/>



Table Of Contents
=================
1. [Overview](#overview)<br>
2. [Table Of Contents](#table-of-contents)<br>
3. [Introduction](#introduction)<br>
4. [How to use](#how-to-use)
6. [References](#references)<br>

Additional Documents
====================
1. [Timeline](docs/timeline.md)




-----------
<a name="how-to-use"/>

How to use
==========
This repository contains sample data extracted from YouTube. The directory structure is as follows:
```
YouReader/                  # custom python package for extracting captions
docs/                       # documents, graphics, and other resources
notebooks/                  # notebooks for graphics
scripts/                    # setup scripts
tests/                      # unit and integration tests
data/                       # collected data
          links.csv         # input file for links
          example.csv       # example input file
          data.json         # downloaded and cleaned data
```
<br>

### Steps (Prerequisites)
Before you can use and test code from this project, you will need the following installed on your system:
* [Python 3.7](https://www.python.org/downloads/)
* [pip - The Python Package Installer](https://pip.pypa.io/en/stable/installing/)
<br>

Optional if you want to generate graphics with notebooks
* [Anaconda](https://www.anaconda.com/products/individual) or [Jupyter Notebook](https://jupyter.org/install.html)
<br>

### Steps (First Time Setup)
To use this package, you'll have to generate a virtual environment to download the prerequisite python libraries.
If you have not generated the virtual environment yet, follow these steps.
1. Download and extract the code
2. Run the following commands:

```
Move to project directory
$ cd GuessTheClass

[Linux, Mac, Windows]
To generate a virtual environment
$ scripts/setup.sh

[Git Bash on Windows]
To generate a virtual environment
$ scripts/winsetup.sh
```
<br>

### Steps (General Setup)
After setting up the virtual environment for the first time,
Run these commands to load up the virtual environment.

```
[Linux, Mac, Windows]
Load the virtual environment
$ source env/bin/activate

[Git Bash on Windows]
Load the virtual environment
$ source env/Scripts/activate

Disable the virtual environment
$ deactivate
```
<br>

### How to run
If you want to run our program and use the existing dataset,
you can run example.py in the project directory

```
$ cd GuessTheClass
$ python3 example.py
```
<br>


If you have your own existing dataset that you want to test,
you can put your video and playlist links into "data/links.csv"
and build an example program like this:

```
from YouReader import Reader

reader = Reader()
dataset = reader.download_csv_captions("../data/links.csv")       # returns a dictionary of transcriptions by video id

for id,data in dataset:
  print(id)                    # unique YouTube video id
  print(data["raw"])           # raw captions
  print(data["clean"])         # cleaned captions
  print(data["link"])          # link to YouTube video
  print(data["notes"])         # notes with the source
```
<br>

-------------------
<a name="preface"/>

-----------------------
<a name="references"/>


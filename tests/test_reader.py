# test_reader.py

#import sys
#sys.path.append("../")
import pytest
from pytube import YouTube

from YouReader.Reader import Reader

# Arrange Section
# ====================================================================

@pytest.fixture
def reader():
    '''Returns a Reader instance with an empty dict'''
    return Reader()

@pytest.fixture
def english_video_links():
    '''Returns list of testable video links'''
    video_links = []
    video_links.append("https://www.youtube.com/watch?v=TQTlCHxyuu8")
    video_links.append("https://www.youtube.com/watch?v=om3n2ni8luE")
    video_links.append("https://www.youtube.com/watch?v=iH08rrt38m8")
    return video_links

@pytest.fixture
def english_video_ids():
    '''Returns matching list of unique id to english_video_links'''
    video_ids = []
    video_ids.append("TQTlCHxyuu8")
    video_ids.append("om3n2ni8luE")
    video_ids.append("iH08rrt38m8")
    return video_ids

@pytest.fixture
def captionless_video_links():
    '''Returns list of videos without en or a.en captions'''
    video_links = []
    video_links.append("https://www.youtube.com/watch?v=5e6F1VA6WG4")
    video_links.append("https://www.youtube.com/watch?v=_OW_bUy0hnE")
    video_links.append("https://www.youtube.com/watch?v=zgIEBsd-OJU")
    video_links.append("https://www.youtube.com/watch?v=Fv1bchdDSG4")
    video_links.append("https://www.youtube.com/watch?v=K2J1c6Qz9fk")
    return video_links

@pytest.fixture
def captionless_video_ids():
    '''Returns matching list of unique id to captionless_video_links'''
    video_ids = []
    video_ids.append("5e6F1VA6WG4")
    video_ids.append("_OW_bUy0hnE")
    video_ids.append("zgIEBsd-OJU")
    video_ids.append("Fv1bchdDSG4")
    video_ids.append("K2J1c6Qz9fk")
    return video_ids

@pytest.fixture
def multilingual_video_links():
    '''Returns list of videos with multiple language captions'''
    video_links = []
    video_links.append("https://www.youtube.com/watch?v=uR8Mrt1IpXg")
    video_links.append("https://www.youtube.com/watch?v=kOHB85vDuow")
    video_links.append("https://www.youtube.com/watch?v=UuV2BmJ1p_I")
    video_links.append("https://www.youtube.com/watch?v=1FqAoADnId4")
    video_links.append("https://www.youtube.com/watch?v=Cp56JdkmE9s")
    return video_links

@pytest.fixture
def multilingual_video_ids():
    '''Returns list of unique id to multilingual_video_links'''
    video_ids = []
    video_ids.append("uR8Mrt1IpXg")
    video_ids.append("kOHB85vDuow")
    video_ids.append("UuV2BmJ1p_I")
    video_ids.append("1FqAoADnId4")
    video_ids.append("Cp56JdkmE9s")
    return video_ids

@pytest.fixture
def multilingual_codes():
    '''Returns matching caption codes to multilingual_video_links'''
    codes = []
    codes.append(["en", "id", "ja", "a.ko", "th"])
    codes.append(["zh-Hans", "en", "a.en", "hi", "ja", "es", "vi"])
    codes.append(["en", "a.fr", "ko"])
    codes.append(["en", "ko", "a.vi"])
    codes.append(["en", "a.ru"])
    return codes


@pytest.fixture
def video_links(english_video_links, captionless_video_links, multilingual_video_links):
    '''Returns concatenated list of english & captionless links'''
    english = english_video_links
    captionless = captionless_video_links
    multilingual = multilingual_video_links
    return english + captionless + multilingual

@pytest.fixture
def video_ids(english_video_ids, captionless_video_ids, multilingual_video_ids):
    '''Returns concatenated list of english & captionless ids parallel to video_links'''
    english = english_video_ids
    captionless = captionless_video_ids
    multilingual = multilingual_video_ids
    return english + captionless + multilingual

@pytest.fixture
def input_entry():
    entry = {}
    entry["subject"] = "music"
    entry["subject name"] = "Bruno Mars Leave the door open mv"
    entry["topic"] = "hot new music i guess"
    entry["link"] = "https://www.youtube.com/watch?v=adLGHcj_fmA"
    entry["notes"] = "bruno mars, anderson paak, silk sonic - leave the door open mv"
    return entry

@pytest.fixture
def fail_entry():
    entry = {}
    entry["link"] = "https://www.youtube.com/watch?v=3UGMDJ9kZCA"
    entry["subject"] = "music"
    entry["notes"] = "nct - 7th sense mv"
    return entry

@pytest.fixture
def raw_caption():
    with open("tests/data/raw_caption.srt") as inFile:
        text = inFile.read()
    return text

@pytest.fixture
def clean_caption():
    with open("tests/data/clean_caption.srt") as inFile:
        text = inFile.read()
    return text

@pytest.fixture
def example_csv():
    return "tests/data/example_links.csv"

@pytest.fixture
def example_json():
    return "tests/data/example_save.json"


# Acts and Asserts
# ================================================================
# Tests that need to be done
# - get_list_subject
# - get_list_clean
# - get_list_raw
# - get_list_link
# - get_list_note
# - load_captions
# - save_captions


def test_default_constructor(reader):
    assert not reader.data

def test_unique_id(reader, video_links, video_ids):
    for link,vid in zip(video_links, video_ids):
        assert reader.__get_unique_id__(link) == vid

def test_unique_link(reader, video_links, video_ids):
    for link,vid in zip(video_links, video_ids):
        assert reader.__get_unique_link__(vid) == link

def test_raw_caption_default(reader, english_video_links):
    for link in english_video_links:
        assert reader.__get_raw_caption__(link) != ""

def test_raw_caption_none(reader, captionless_video_links):
    for link in captionless_video_links:
        assert reader.__get_raw_caption__(link) == ""

def test_clean_caption(reader, raw_caption, clean_caption):
    assert reader.__get_clean_caption__(raw_caption).split() == clean_caption.split()

def test_generate_entry_with_captions(reader, input_entry):
    entry = reader.__generate_entry__(input_entry)
    assert entry["subject"] == input_entry["subject"]
    assert entry["subject name"] == input_entry["subject name"]
    assert entry["topic"] == input_entry["topic"]
    assert entry["link"] == input_entry["link"]
    assert entry["notes"] == input_entry["notes"]
    assert entry["raw"] != ""
    assert entry["clean"] != ""

def test_generate_entry_no_captions(reader, fail_entry):
    assert reader.__generate_entry__(fail_entry)["clean"] == ""

def test_download_csv_captions(reader, example_csv, example_json):
    reader.download_csv_captions(csv_file=example_csv, savefile=example_json)
    assert reader.data

if __name__ == "__main__":
    print("To run this test, use 'pytest'")

# test_reader.py

import sys
sys.path.append("../")
import pytest
from YouReader import Reader



@pytest.fixture
def default_reader():
    '''Returns a Reader instance with an empty dict'''
    return Reader()

@pytest.fixture
def english_video_links():
    '''Returns list of testable video links'''
    video_links = []
    return "https://www.youtube.com/watch?v=5h3sIRrQHJE"

def english_video_id():
    '''Returns matching list of unique id to english_video_links'''
    video_id = []

def test_default_constructor(default_reader):
    assert not default_reader.data


if __name__ == "__main__":
    test_default_constructor(default_reader)

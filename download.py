from YouReader.Reader import Reader
from YouReader.Constants import path

if __name__ == "__main__":
    reader = Reader()
    reader.download_csv_captions(path.EXAMPLE)
    count = reader.save_captions(path.SAVE)	
    print("Saved ", count, " video transcriptions!")

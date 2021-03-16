from YouReader.Reader import Reader
from YouReader.Constants import path

if __name__ == "__main__":
    reader = Reader()
    reader.load_captions()
    reader.download_csv_captions(verbose=True, threads=12)
    count = reader.save_captions(path.SAVE)	
    print("Saved ", count, " video transcriptions!")

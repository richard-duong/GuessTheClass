# standard libraries
import ntpath
import os


class PathHandler:

    def __init__(self):
        pass

    
    # gets the base file or foldername from the path
    def path_leaf(self, path):
        head, tail = ntpath.split(path)
        return tail or ntpath.basename(head)
        

    # get list of all subdirectory paths from src_path
    def get_dir_paths(self, src_path):
        dir_paths = []
        for dir_path in glob.glob(src_path + "*/"):
            dir_paths.append(dir_path)
        return dir_paths


    # get list of all subdirectory names from src_path
    def get_dir_names(self, src_path):
        dir_names = []
        dir_paths = self.get_dir_paths(src_path)
        for dir_path in dir_paths:
            dir_name = self.path_leaf(dir_path)
            dir_names.append(dir_name)
        return dir_names


    # get list of all subfile paths from src_path
    def get_file_paths(self, src_path):
        file_paths = []
        for file_path in glob.glob(src_path + "*.*"):
            file_paths.append(file_path)
        return file_paths


    # get list of all subfile names from src_path
    def get_file_names(self, src_path):
        file_names = []
        file_paths = self.get_file_paths(src_path)
        for file_path in file_paths:
            file_name = self.path_leaf(file_path)
            file_names.append(file_name)
        return file_names
    

    # builds subdirectories to dest_path if not existing compared to src_path
    def build_matching_subdir(self, src_path, dest_path):
        src_dirs = self.get_dir_names(src_path)
        dest_dirs = self.get_dir_names(dest_path)
        for dir_name in src_dirs:
            if dir_name not in dest_dirs:
                os.mkdir(dest_path + dir_name)


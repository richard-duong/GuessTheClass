import paths
from PathHandler import PathHandler

pather = PathHandler()

pather.get_dir_names(paths.RAW)
pather.get_dir_paths(paths.RAW)

pather.get_file_names(paths.RAW + "CS/")
pather.get_file_paths(paths.RAW + "CS/")

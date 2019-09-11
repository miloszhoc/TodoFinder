import os
import sys


class CatalogWalker:
    def __init__(self, path, extension, excluded):
        self.path_sep = '\\' if sys.platform == 'win32' else '/'
        self.path = path + self.path_sep
        self.files_in_path = self._get_files_from_path(path)
        self.excluded = excluded if excluded is not None else ''
        self.extension = extension

    def _get_files_from_path(self, p: str) -> list:
        return os.listdir(p)

    def _file_searcher(self, path, files: list) -> list:
        found_files = []
        files = [path + file for file in files if file not in self.excluded]
        for file in files:
            isdir = os.path.isdir(file)
            if isdir:
                found_files.extend(self._file_searcher(file + self.path_sep, self._get_files_from_path(file)))
            elif file.endswith('{}'.format(self.extension)):
                found_files.append(file)
        return found_files

    def walk(self):
        return self._file_searcher(self.path, self.files_in_path)

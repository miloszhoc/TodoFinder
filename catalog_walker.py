import os
import sys


class CatalogWalker:
    def __init__(self, main_path: str, extension: str, excluded: tuple):
        self._path_sep = '\\' if sys.platform == 'win32' else '/'
        self._path = main_path if main_path.endswith('\\') or \
                                  main_path.endswith('/') else main_path + self._path_sep
        self._files_in_path = self._get_files_from_path(main_path)
        self._excluded = excluded if excluded is not None else ''
        self._extension = extension

    def _get_files_from_path(self, p: str) -> list:
        return os.listdir(p)

    def _file_searcher(self, path, files: list) -> list:
        found_files = []
        files = [path + file for file in files if file not in self._excluded]
        for file in files:
            isdir = os.path.isdir(file)
            if isdir:
                found_files.extend(self._file_searcher(file + self._path_sep, self._get_files_from_path(file)))
            elif file.endswith('{}'.format(self._extension)):
                found_files.append(file)
        return found_files

    def walk(self) -> _file_searcher:
        return self._file_searcher(self._path, self._files_in_path)

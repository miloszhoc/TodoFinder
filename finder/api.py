from exceptions.exceptions import *
from finder.comment_sign import ext_to_comment_sign
from finder.catalog_walker import CatalogWalker
from finder.todo_searcher import TodoSearcher


class Api:
    @staticmethod
    def find_in_file(f_name: str, todo: bool, fixme: bool):
        ext = '.' + f_name.split('.')[1]  # fixme find better way to get extension
        try:
            comment_sign = ext_to_comment_sign(ext)
        except CommentSignNotFound as e:
            print(e.message)
        else:
            searcher = TodoSearcher(todo=todo, fixme=fixme, comment_sign=comment_sign)
            searcher.search(f_name)

    @staticmethod
    def find_in_catalog(ext: str, path, exclude, todo: bool, fixme: bool):
        try:
            comment_sign = ext_to_comment_sign(ext.lower())
            files = CatalogWalker(path, ext, exclude)

            searcher = TodoSearcher(todo, fixme, comment_sign)

        except CommentSignNotFound as e:
            print(e.message)
        except FileNotFoundError:
            print('Path does not exist')
        except NotADirectoryError:
            print('Not a directory')
        else:
            for file in files.walk():
                searcher.search(file)

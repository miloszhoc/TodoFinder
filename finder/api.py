from exceptions.exceptions import *
from finder.comment_sign import ext_to_comment_sign
from finder.catalog_walker import CatalogWalker
from finder.todo_searcher_single import TodoSearcherS
from finder.todo_searcher_multi import TodoSearcherM


class Api:
    @staticmethod
    def find_in_file(files: list, todo: bool, fixme: bool) -> None:
        """
        Finds todo and fixme in given file on files
        :param files: list of paths to files which contains todos
        :param todo: if True find todo
        :param fixme: if True find fixme
        :return: None
        """
        for file in files:
            ext = '.' + file.split('.')[-1]
            try:
                comment_sign = ext_to_comment_sign(ext.lower())
                # if language supports only single line comments
                # comment_sign is instance of string
                #
                # if language supports multilines comments
                # comment_sign is instance of tuple which contains
                # (single line comment sign, multiline comment sing for start
                # and end of the comment)
                if comment_sign['multi']:

                    comment_sign = (comment_sign['single'], comment_sign['multi'][0], comment_sign['multi'][1])

                    searcher = TodoSearcherM(todo=todo,
                                             fixme=fixme,
                                             comment_sign=comment_sign)
                    searcher.search(file, single_file=True)
                else:
                    comment_sign = comment_sign['single']
                    searcher = TodoSearcherS(todo=todo,
                                             fixme=fixme,
                                             comment_sign=comment_sign)
                    searcher.search(file, single_file=True)
            except CommentSignNotFound as e:
                print(e.message)

    @staticmethod
    def find_in_catalog(ext: str, path: str, exclude: tuple, todo: bool, fixme: bool) -> None:
        """
        Find todo and fixme in given catalog.
        :param ext: Files extension.
        :param path: Path to catalog
        :param exclude: Exclude given folders and files.
        :param todo: if True find todo
        :param fixme: if True find fixme
        :return: None
        """
        try:
            comment_sign = ext_to_comment_sign(ext.lower())
            if comment_sign['multi']:  # fixme same code as above
                comment_sign = (comment_sign['single'], comment_sign['multi'][0], comment_sign['multi'][1])
                files = CatalogWalker(path, ext, exclude)
                searcher = TodoSearcherM(todo=todo,
                                         fixme=fixme,
                                         comment_sign=comment_sign)
            else:
                comment_sign = comment_sign['single']
                files = CatalogWalker(path, ext, exclude)
                searcher = TodoSearcherS(todo=todo,
                                         fixme=fixme,
                                         comment_sign=comment_sign)
        except CommentSignNotFound as e:
            print(e.message)
        except FileNotFoundError:
            print('Path does not exist')
        except NotADirectoryError:
            print('Not a directory')
        else:
            files = files.walk()
            searcher.search(files)

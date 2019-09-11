import argparse
from exceptions.exceptions import *
from comment_sign import ext_to_comment_sign
from catalog_walker import CatalogWalker
from todo_searcher import TodoSearcher


# todo add support for multiple file extensions
def main():
    # todo add support for single file
    parser = argparse.ArgumentParser(description='Todo and Fixme finder')
    parser.add_argument('path', action='store', help='path to catalog')
    parser.add_argument('ext', action='store', help='file extension')
    parser.add_argument('-f', '--fixme', action='store_true', help='show only FIXME')
    parser.add_argument('-t', '--todo', action='store_true', help='show only TODO')
    parser.add_argument('-e', '--exclude', action='store', help='excluded files and folders', nargs='*')

    args = parser.parse_args()

    try:
        comment_sign = ext_to_comment_sign(args.ext.lower())
    except CommentSignNotFound as e:
        print(e.message)
    else:
        files = CatalogWalker(args.path, args.ext, args.exclude)

        searcher = TodoSearcher(args.todo, args.fixme, comment_sign)

        for file in files.walk():
            searcher.search(file)


if __name__ == '__main__':
    main()

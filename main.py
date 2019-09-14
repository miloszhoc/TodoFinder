import argparse
from finder.api import Api


# todo add support for multiline comments
# todo add support for multiple file extensions
def main():
    parser = argparse.ArgumentParser(description='Todo and Fixme finder')

    subparsers = parser.add_subparsers(dest='subparser_name')

    one_file = subparsers.add_parser('file', help='show todo/fixme for one file')
    one_file.add_argument('file_name', action='store', help='file to open')
    one_file.add_argument('-f', '--fixme', action='store_true', help='show only FIXME')
    one_file.add_argument('-t', '--todo', action='store_true', help='show only TODO')

    catalog = subparsers.add_parser('catalog', help='show todo/fixme for all files in catalog')
    catalog.add_argument('path', action='store', help='path to catalog')
    catalog.add_argument('ext', action='store', help='file extension')
    catalog.add_argument('-f', '--fixme', action='store_true', help='show only FIXME')
    catalog.add_argument('-t', '--todo', action='store_true', help='show only TODO')
    catalog.add_argument('-e', '--exclude', action='store', help='excluded files and folders', nargs='*')

    args = parser.parse_args()

    if args.subparser_name == 'file':
        Api.find_in_file(args.file_name, args.todo, args.fixme)
    elif args.subparser_name == 'catalog':
        Api.find_in_catalog(args.ext, args.path, args.exclude, args.todo, args.fixme)

    else:
        print('todo and fixme finder')


if __name__ == '__main__':
    main()

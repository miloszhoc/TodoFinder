import os
import re
import argparse
import sys
from typing import List
from exceptions.exceptions import *


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
    # args = parser.parse_args(['.', '.py', '-f', '-t', '-e', 'venv', '.git', '.idea'])

    path_separator = '\\' if sys.platform == 'win32' else '/'

    path = args.path + path_separator  # root catalog path
    files_in_path = get_files_from_path(path)
    excluded = args.exclude if args.exclude is not None else ''
    extension = args.ext
    try:
        comment_sign = ext_to_comment_sign(extension)
    except SignNotFound as e:
        print(e.message)
    else:
        py_files = file_searcher(path, files_in_path, extension, excluded, path_separator)

        if (not args.fixme and not args.todo) or (args.todo and args.fixme):
            for file in py_files:
                find_todo_and_fixme_in_file(file, comment_sign)
        elif args.fixme:
            for file in py_files:
                find_fixme_in_file(file, comment_sign)
        elif args.todo:
            for file in py_files:
                find_todo_in_file(file, comment_sign)


def find_todo_in_file(file_name: str, comment_sign: str) -> None:
    with open(file_name, 'r', encoding='utf-8') as f:
        i = 0
        for line in f:
            i += 1
            pattern = re.search('{} ?[Tt][Oo][Dd][Oo].+'.format(comment_sign), line)
            if pattern:
                print('line: ' + str(i) + ' ' + f.name + ' \n ' + pattern[0] + '\n')


def find_fixme_in_file(file_name: str, comment_sign: str) -> None:
    with open(file_name, 'r', encoding='utf-8') as f:
        i = 0
        for line in f:
            i += 1
            pattern = re.search('{} ?[Ff][Ii][Xx] ?[Mm][Ee].+'.format(comment_sign), line)
            if pattern:
                print('line: ' + str(i) + ' ' + f.name + ' \n ' + pattern[0] + '\n')


def find_todo_and_fixme_in_file(file_name: str, comment_sign: str) -> None:
    with open(file_name, 'r', encoding='utf-8') as f:
        i = 0
        for line in f:
            i += 1
            pattern = re.search('{} ?(([Tt][Oo][Dd][Oo].+)|([Ff][Ii][Xx][Mm][Ee].+))'.format(comment_sign), line)
            if pattern:
                print('line: ' + str(i) + ' ' + f.name + ' \n ' + pattern[0] + '\n')


# todo: add more extensions
def ext_to_comment_sign(ext):
    signs = {'.py': '#',
             '.java': '//',
             '.xml': '<!--',
             '.html': '<!--',
             '.htm': '<!--',
             '.c': '//',
             '.cs': '//',
             '.cpp': '//',
             '.css': '//',
             '.go': '//',
             '.php': '//',
             '.js': '//',
             '.hs': '--',
             '.m': '%',
             '.sh': '#', }
    if ext in signs:
        return signs[ext]
    else:
        raise SignNotFound


def get_files_from_path(p: str) -> list:
    return os.listdir(p)


def file_searcher(path: str, files: List[str], f_ext: str, excluded: tuple, path_sep: str) -> list:
    py = []
    files = [path + file for file in files if file not in excluded]
    for file in files:
        isdir = os.path.isdir(file)
        if isdir:
            py.extend(file_searcher(file + path_sep, os.listdir(file), f_ext, excluded, path_sep))
        elif file.endswith('{}'.format(f_ext)):
            py.append(file)
    return py


if __name__ == '__main__':
    main()

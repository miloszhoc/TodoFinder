import re
import chardet


class TodoSearcherM:
    def __init__(self, todo: bool, fixme: bool, comment_sign):
        self._todo = todo
        self._fixme = fixme
        self._comment_sign = comment_sign

    def _detect_encoding(self, file_name: str):
        with open(file_name, 'rb') as f:
            return chardet.detect(f.read())['encoding']

    def _set_regex_single(self) -> str:
        if self._todo and not self._fixme:
            return '{}.*[Tt][Oo][Dd][Oo].*'.format(self._comment_sign[0])
        elif self._fixme and not self._todo:
            return '{}.*[Ff][Ii][Xx] ?[Mm][Ee].*'.format(self._comment_sign[0])
        else:
            return '{}.*(([Tt][Oo][Dd][Oo].+)|([Ff][Ii][Xx][Mm][Ee].*))'.format(self._comment_sign[0])

    def _set_regex_multi(self) -> str:
        if self._todo and not self._fixme:
            return '[Tt][Oo][Dd][Oo].*'
        elif self._fixme and not self._todo:
            return '[Ff][Ii][Xx] ?[Mm][Ee].*'
        else:
            return '(([Tt][Oo][Dd][Oo].+)|([Ff][Ii][Xx][Mm][Ee].*))'

    def _read_file(self, file_name: str, encoding: str, error: str):
        with open(file_name, 'r', encoding=encoding, errors=error) as f:
            i = 0
            for line in f:
                i += 1
                yield line, i, f.name

    def _finder(self, file_name: str, regex_s: str, regex_m: str, encoding: str, error: str):
        file = self._read_file(file_name, encoding, error)
        for line in file:
            pattern = re.search(regex_s, line[0])
            if pattern:
                print('line: ' + str(line[1]) + ' ' + line[2] + ' \n ' + pattern[0] + '\n')

            # if file contains multiline comment
            # program searches for multiline comment symbol in file
            # and appends lines until end of comment
            elif self._comment_sign[1] in line[0]:
                text = []
                try:
                    while self._comment_sign[2] not in line[0]:
                        text.append((line[0], line[1]))
                        line = next(file)
                    next(file)
                except StopIteration:
                    pass
                finally:
                    text.append((line[0], line[1]))
                for i in text:
                    pattern_multi = re.search(regex_m, i[0])
                    if pattern_multi:
                        print('line: ' + str(i[1]) + ' ' + line[2] + ' \n ' + pattern_multi[0] + '\n')

    def search(self, f_name: list and str, single_file=None):
        regex_s = self._set_regex_single()
        regex_m = self._set_regex_multi()
        if single_file:
            encoding = 'utf-8'
            try:
                self._finder(f_name, regex_s, regex_m, encoding, 'strict')
            except UnicodeDecodeError:
                encoding = self._detect_encoding(f_name)
                self._finder(f_name, regex_s, regex_m, encoding, 'ignore')
        else:
            for file in f_name:
                try:
                    encoding = 'utf-8'
                    self._finder(file, regex_s, regex_m, encoding, 'strict')
                except UnicodeDecodeError:
                    encoding = self._detect_encoding(file)
                    self._finder(file, regex_s, regex_m, encoding, 'ignore')

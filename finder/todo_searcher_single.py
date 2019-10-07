import re
import chardet


# fixme self.assertRegex('# todo test', regex) shouldn't find anything
class TodoSearcher:
    def __init__(self, todo: bool, fixme: bool, comment_sign: str):
        self._todo = todo
        self._fixme = fixme
        self._comment_sign = comment_sign

    def _detect_encoding(self, file_name: str):
        with open(file_name, 'rb') as f:
            return chardet.detect(f.read())['encoding']

    def _set_regex(self) -> str:
        if self._todo and not self._fixme:
            return '{}.*[Tt][Oo][Dd][Oo].*'.format(self._comment_sign)
        elif self._fixme and not self._todo:
            return '{}.*[Ff][Ii][Xx] ?[Mm][Ee].*'.format(self._comment_sign)
        else:
            return '{}.*(([Tt][Oo][Dd][Oo].+)|([Ff][Ii][Xx][Mm][Ee].*))'.format(self._comment_sign)

    def _finder(self, file_name: str, regex: str, encoding: str, error: str):
        with open(file_name, 'r', encoding=encoding, errors=error) as f:
            i = 0
            for line in f:
                i += 1
                pattern = re.search(regex, line)
                if pattern:
                    print('line: ' + str(i) + ' ' + f.name + ' \n ' + pattern[0] + '\n')

    # Method searches for regex in current file
    # and tries to open each file in utf-8 encoding.
    # If file raises UnicodeDecodeError, chardet library is trying
    # to determine encoding. If that method fails error is ignored.
    def search(self, f_name: list and str, single_file=None):  # fixme f_name type
        regex = self._set_regex()
        if single_file:
            encoding = 'utf-8'
            try:
                self._finder(f_name, regex, encoding, 'strict')
            except UnicodeDecodeError:
                encoding = self._detect_encoding(f_name)
                self._finder(f_name, regex, encoding, 'ignore')
        else:
            for file in f_name:
                try:
                    encoding = 'utf-8'
                    self._finder(file, regex, encoding, 'strict')
                except UnicodeDecodeError:
                    encoding = self._detect_encoding(file)
                    self._finder(file, regex, encoding, 'ignore')

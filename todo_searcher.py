import re


class TodoSearcher:
    def __init__(self, todo: bool, fixme: bool, comment_sign: str):
        self._todo = todo
        self._fixme = fixme
        self._comment_sign = comment_sign

    def _set_regex(self) -> str:
        if self._todo and not self._fixme:
            return '{} ?[Tt][Oo][Dd][Oo].+'.format(self._comment_sign)
        elif self._fixme and not self._todo:
            return '{} ?[Ff][Ii][Xx] ?[Mm][Ee].+'.format(self._comment_sign)
        else:
            return '{} ?(([Tt][Oo][Dd][Oo].+)|([Ff][Ii][Xx][Mm][Ee].+))'.format(self._comment_sign)

    def _finder(self, file_name: str, regex: str):
        with open(file_name, 'r', encoding='utf-8') as f:
            i = 0
            for line in f:
                i += 1
                pattern = re.search(regex, line)
                if pattern:
                    print('line: ' + str(i) + ' ' + f.name + ' \n ' + pattern[0] + '\n')

    def search(self, file_name: str):
        regex = self._set_regex()
        self._finder(file_name, regex)

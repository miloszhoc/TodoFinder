import re


class TodoSearcher:
    def __init__(self, todo, fixme, comment_sign):
        self.todo = todo
        self.fixme = fixme
        self.comment_sign = comment_sign

    def _set_regex(self, todo=False, fixme=False):
        if todo and not fixme:
            return '{} ?[Tt][Oo][Dd][Oo].+'.format(self.comment_sign)
        elif fixme and not todo:
            return '{} ?[Ff][Ii][Xx] ?[Mm][Ee].+'.format(self.comment_sign)
        else:
            return '{} ?(([Tt][Oo][Dd][Oo].+)|([Ff][Ii][Xx][Mm][Ee].+))'.format(self.comment_sign)

    def _finder(self, file_name: str, regex: str):
        with open(file_name, 'r', encoding='utf-8') as f:
            i = 0
            for line in f:
                i += 1
                pattern = re.search(regex, line)
                if pattern:
                    print('line: ' + str(i) + ' ' + f.name + ' \n ' + pattern[0] + '\n')

    def search(self, file_name):
        regex = self._set_regex(self.todo, self.fixme)
        self._finder(file_name, regex)

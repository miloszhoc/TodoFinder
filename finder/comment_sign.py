from exceptions.exceptions import *


# todo: add more extensions
def ext_to_comment_sign(ext: str):
    signs = {('.py', '.sh'): {'single': '#', 'multi': None},
             ('.java', '.c', '.cs', '.cpp', '.css', '.go', '.php', '.js'): {'single': '//',
                                                                            'multi': ('/*', '*/')},
             ('.xml', '.html', '.htm'): {'single': '<!--',
                                         'multi': ('<!--', '-->')},
             ('.hs',): {'single': '--',
                        'multi': None},
             ('.m',): {'single': '%',
                       'multi': ('%{', '%}')}}
    for k, v in signs.items():
        if ext in k:
            return v
    else:
        raise CommentSignNotFound

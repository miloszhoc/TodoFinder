from exceptions.exceptions import *


# todo: add more extensions
def ext_to_comment_sign(ext: str):
    """
    Matches file extension with suitable comment sign.

    :param ext: file extension with leading dot (eg '.py')
    :return: single and multiline comment signs
    """
    signs = {('.py', '.sh'): {'single': '#', 'multi': None},
             ('.java', '.c', '.cs', '.cpp', '.css', '.go', '.php', '.js'): {'single': '//',
                                                                            'multi': ('/*', '*/')},
             ('.xml', '.html', '.htm'): {'single': '<!--',
                                         'multi': ('<!--', '-->')},
             ('.hs',): {'single': '--',
                        'multi': None},
             ('.m',): {'single': '%',
                       'multi': ('%{', '%}')}}
    for extension, sign in signs.items():
        if ext in extension:
            return sign
    else:
        raise CommentSignNotFound

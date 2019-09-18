from exceptions.exceptions import *


# todo: add more extensions
def ext_to_comment_sign(ext: str):
    signs = {('.py', '.sh'): '#',
             ('.java', '.c', '.cs', '.cpp', '.css', '.go', '.php', '.js'): '//',
             ('.xml', '.html', '.htm'): '<!--',
             ('.hs',): '--',
             ('.m',): '%'}
    for k, v in signs.items():
        if ext in k:
            return v
    else:
        raise CommentSignNotFound

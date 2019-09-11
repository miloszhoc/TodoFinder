class FinderExceptions(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message


class CommentSignNotFound(FinderExceptions):
    def __init__(self):
        super().__init__('Comment sign for given file extension not found')

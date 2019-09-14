import unittest
from todo_searcher import TodoSearcher


class TestTodoSearcher(unittest.TestCase):
    def test_set_regex_when_todo_true(self):
        todo = TodoSearcher(todo=True, fixme=False, comment_sign='#')
        regex = todo._set_regex()
        self.assertRegex('# todo test', regex)

    def test_set_regex_when_fixme_true(self):
        fixme = TodoSearcher(todo=False, fixme=True, comment_sign='//')
        regex = fixme._set_regex()
        self.assertRegex("// fixme test", regex)

    def test_set_regex_when_todo_and_fixme_true(self):
        todo_fixme = TodoSearcher(todo=True, fixme=True, comment_sign='//')
        regex = todo_fixme._set_regex()
        self.assertRegex("// fixme test, #TODO: test2", regex)

import unittest
from finder.catalog_walker import CatalogWalker
import os

main_path = os.path.join('tests', 'catalog_to_test')


class TestCatalogWalker(unittest.TestCase):
    def test_init_when_main_path_does_not_exists(self):
        walker = CatalogWalker
        self.assertRaises(FileNotFoundError, walker, 'w', '.py', ('',))

    def test_init_when_main_path_exists(self):
        walker = CatalogWalker('.', '.py', ('',))
        self.assertGreater(len(walker._files_in_path), 0)

    def test_init_when_main_path_is_not_a_directory(self):
        walker = CatalogWalker
        self.assertRaises(NotADirectoryError, walker, os.path.join(main_path, 'file_in_catalog.py'), '.py', ('',))

    def test_init_when_excluded_is_None(self):
        walker = CatalogWalker('.', '.py', None)
        self.assertEqual(walker._excluded, '')

    def test_walk_when_one_file_is_excluded(self):
        walker = CatalogWalker(main_path, '.py', ('file_in_catalog.py',))
        self.assertListEqual(walker.walk(), [os.path.join(main_path, 'a', 'a1', 'file_in_a1.py'),
                                             os.path.join(main_path, 'a', 'file2_in_a.py'),
                                             os.path.join(main_path, 'b', 'b1', 'b2', 'file_in_b2.py')])

    def test_walk_when_catalog_is_excluded(self):
        walker = CatalogWalker(main_path, '.py', ('a',))
        self.assertListEqual(walker.walk(), [os.path.join(main_path, 'b', 'b1', 'b2', 'file_in_b2.py'),
                                             os.path.join(main_path, 'file_in_catalog.py')])

    def test_walk_when_more_than_one_catalog_is_excluded(self):
        walker = CatalogWalker(main_path, '.py', ('a', 'b'))
        self.assertListEqual(walker.walk(), [os.path.join(main_path, 'file_in_catalog.py')])

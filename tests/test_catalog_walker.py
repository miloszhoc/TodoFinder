import unittest
from finder.catalog_walker import CatalogWalker
import sys

platform = sys.platform
main_path = 'tests\\catalog_to_test\\' if platform == 'win32' else 'tests/catalog_to_test/'


class TestCatalogWalker(unittest.TestCase):
    def test_init_when_main_path_does_not_exists(self):
        walker = CatalogWalker
        self.assertRaises(FileNotFoundError, walker, 'w', '.py', ('',))

    def test_init_when_main_path_exists(self):
        walker = CatalogWalker('.', '.py', ('',))
        self.assertGreater(len(walker._files_in_path), 0)

    def test_init_when_main_path_is_not_a_directory(self):
        walker = CatalogWalker
        self.assertRaises(NotADirectoryError, walker, main_path + 'file_in_catalog.py', '.py', ('',))

    def test_init_when_excluded_is_None(self):
        walker = CatalogWalker('.', '.py', None)
        self.assertEqual(walker._excluded, '')

    def test_walk_when_one_file_is_excluded(self):
        walker = CatalogWalker(main_path, '.py', ('file_in_catalog.py',))
        if platform == 'win32':
            self.assertListEqual(walker.walk(), ['tests\\catalog_to_test\\a\\a1\\file_in_a1.py',
                                                 'tests\\catalog_to_test\\a\\file2_in_a.py',
                                                 'tests\\catalog_to_test\\b\\b1\\b2\\file_in_b2.py'])
        else:
            self.assertListEqual(walker.walk(), ['tests/catalog_to_test/a/a1/file_in_a1.py',
                                                 'tests/catalog_to_test/a/file2_in_a.py',
                                                 'tests/catalog_to_test/b/b1/b2/file_in_b2.py'])

    def test_walk_when_catalog_is_excluded(self):
        walker = CatalogWalker(main_path, '.py', ('a',))
        if platform == 'win32':
            self.assertListEqual(walker.walk(), ['tests\\catalog_to_test\\b\\b1\\b2\\file_in_b2.py',
                                                 'tests\\catalog_to_test\\file_in_catalog.py'])
        else:
            self.assertListEqual(walker.walk(), ['tests/catalog_to_test/b/b1/b2/file_in_b2.py',
                                                 'tests/catalog_to_test/file_in_catalog.py'])

    def test_walk_when_more_than_one_catalog_is_excluded(self):
        walker = CatalogWalker(main_path, '.py', ('a', 'b'))
        if platform == 'win32':
            self.assertListEqual(walker.walk(), ['tests\\catalog_to_test\\file_in_catalog.py'])
        else:
            self.assertListEqual(walker.walk(), ['tests/catalog_to_test/file_in_catalog.py'])

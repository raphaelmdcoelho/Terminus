# test_filters.py

import unittest
import filters


class TestFilters(unittest.TestCase):

    def test_filter_empty_rows(self):
        data = [['Contador', '110.00'], [], ['Seguro do Carro', '304.78']]
        expected = [['Contador', '110.00'], ['Seguro do Carro', '304.78']]
        self.assertEqual(filters.filter_empty_rows(data), expected)

    def test_filter_rows_after_total(self):
        data = [['a'], ['b'], ['Total'], ['c'], ['d']]
        expected = [['a'], ['b']]
        self.assertEqual(filters.filter_rows_after_total(data), expected)

        data = [['a'], ['b'], ['total'], ['c'], ['d']]
        expected = [['a'], ['b']]
        self.assertEqual(filters.filter_rows_after_total(data), expected)

    def test_apply_all_filters(self):
        data = [['a'], [], ['Total'], [], ['d']]
        expected = [['a']]
        self.assertEqual(filters.apply_all_filters(data), expected)


if __name__ == '__main__':
    unittest.main()

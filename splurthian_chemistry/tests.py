import unittest

from splurthian_chemistry.splurth import *


class SplurthianElementSymbolTest(unittest.TestCase):

    def test_valid_element_symbols(self):
        self.assertTrue(check_element_symbol('Spenglerium', 'Ee'))
        self.assertTrue(check_element_symbol('Zeddemorium', 'Zr'))
        self.assertTrue(check_element_symbol('Venkmine', 'Kn'))

    def test_invalid_element_symbols(self):
        self.assertFalse(check_element_symbol('Stantzon', 'Zt'))
        self.assertFalse(check_element_symbol('Melintzum', 'Nn'))
        self.assertFalse(check_element_symbol('Tullium', 'Ty'))

    def test_invalid_case_symbols(self):
        self.assertFalse(check_element_symbol('Spenglerium', 'ee'))
        self.assertFalse(check_element_symbol('Zeddemorium', 'zR'))
        self.assertFalse(check_element_symbol('Venkmine', 'KN'))

    def test_list_all_valid_symbols(self):
        self.assertCountEqual(list_all_symbols_for_element('Aaaaaba'), ['Aa', 'Ab', 'Ba'])
        self.assertCountEqual(list_all_symbols_for_element('Aaaa'), ['Aa'])

    def test_first_alphabetical_symbol(self):
        self.assertEqual(find_first_alphabetical_valid_symbol('Gozerium'), 'Ei')
        self.assertEqual(find_first_alphabetical_valid_symbol('Slimyrine'), 'Ie')

    def test_count_valid_symbols(self):
        self.assertEqual(count_all_symbols_for_element('Zuulon'), 11)


class BlurthianSymbolTest(unittest.TestCase):

    def test_count_blurthian_symbols(self):
        self.assertEqual(count_blurthian_symbols('Zuulon'), 47)


if __name__ == '__main__':
    unittest.main()

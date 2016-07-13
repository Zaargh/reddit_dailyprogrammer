import unittest

from splurthian_chemistry.splurth import check_element_symbol, list_all_symbols_for_element


class SplurthianElementSymbolTest(unittest.TestCase):

    def test_valid_element_symbols(self):
        self.assertTrue(check_element_symbol('Spenglerium', 'Ee'))
        self.assertTrue(check_element_symbol('Zeddemorium', 'Zr'))
        self.assertTrue(check_element_symbol('Venkmine', 'Kn'))

    def test_invalid_element_symbols(self):
        self.assertFalse(check_element_symbol('Stantzon', 'Zt'))
        self.assertFalse(check_element_symbol('Melintzum', 'Nn'))
        self.assertFalse(check_element_symbol('Tullium', 'Ty'))

    def test_list_all_valid_symbols(self):
        self.assertCountEqual(list_all_symbols_for_element('Aaaaaba'), ['Aa', 'Ab', 'Ba'])
        self.assertCountEqual(list_all_symbols_for_element('Aaaa'), ['Aa'])

if __name__ == '__main__':
    unittest.main()

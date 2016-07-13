import unittest

from splurth import check_element_symbol


class SplurthianElementSymbolTest(unittest.TestCase):

    def test_valid_element_symbols(self):
        self.assertTrue(check_element_symbol('Spenglerium', 'Ee'))
        self.assertTrue(check_element_symbol('Zeddemorium', 'Zr'))
        self.assertTrue(check_element_symbol('Venkmine', 'Kn'))

    def test_invalid_element_symbols(self):
        self.assertFalse(check_element_symbol('Stantzon', 'Zt'))
        self.assertFalse(check_element_symbol('Melintzum', 'Nn'))
        self.assertFalse(check_element_symbol('Tullium', 'Ty'))


if __name__ == '__main__':
    unittest.main()

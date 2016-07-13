import re
import itertools


def check_element_symbol(name, symbol):
    """
    Checks if symbol is valid for the element
    :param name: Element name
    :param symbol: Validated symbol
    :return: True if symbol is valid, False otherwise
    """
    # valid symbol has exactly 2 chars
    if not len(symbol) == 2:
        return False

    symbol_in_name_re = re.compile(r'.*{0}.*{1}.*'.format(symbol[0], symbol[1]), re.I)
    if symbol_in_name_re.match(name):
        return True
    else:
        return False


def list_all_symbols_for_element(name):
    """
    Creates list of all valid symbols for an element
    :param name: Element name
    :return: List of all valid symbols (unsorted)
    """

    if len(name) < 2:
        raise ValueError('Element name must be at least 2 chars long')

    result = set()
    for i, _ in enumerate(name, start=0):
        for pair in itertools.product(name[:i], name[i:]):
            result.add(''.join(pair).capitalize())
    return result

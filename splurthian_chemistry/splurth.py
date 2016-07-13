import re


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

    correct_symbol_re = re.compile(r'.*{0}.*{1}.*'.format(symbol[0], symbol[1]), re.I)
    if correct_symbol_re.match(name):
        return True
    else:
        return False

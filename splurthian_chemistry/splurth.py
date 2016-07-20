import re
import itertools
import operator
import collections


def check_element_symbol(name, symbol):
    """
    Checks if symbol is valid for the element
    :param name: Element name
    :param symbol: Validated symbol
    :return: True if symbol is valid, False otherwise
    """
    # valid symbol has exactly 2 chars
    if not len(symbol) == 2 or not symbol.istitle():
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


def find_first_alphabetical_valid_symbol(name):
    return sorted(list_all_symbols_for_element(name))[0]


def count_all_symbols_for_element(name):
    return len(list_all_symbols_for_element(name))


def count_blurthian_symbols(name):
    if len(name) < 2:
        raise ValueError('Element name must be at least 2 chars long')

    result = set()
    for i, _ in enumerate(name, start=1):
        possibilities = [''.join(p).capitalize() for p in itertools.combinations(name, i)]
        result.update(possibilities)
    return len(result)


def symbol_score(name, symbol):
    first_score = name.lower().index(symbol.lower()[0])
    second_score = name.lower()[first_score+1:].index(symbol.lower()[1]) + first_score + 1
    return first_score, second_score


def symbols_sorted_by_score(name):
    symbols = list_all_symbols_for_element(name)
    symbols_rated = [(s, symbol_score(name, s)) for s in symbols]
    return [s[0] for s in sorted(symbols_rated, key=operator.itemgetter(1))]


def match_splurthian_symbols_to_element_list(fname):
    """
    Assigns symbols to list of elements, according to rules in Splurthian Chemistry 102 challenge.
    If valid symbol cannot be assigned for an element None is assigned.
    :return: collections.OrderedDict {name: symbol}.
    """

    with open(fname, 'r') as f:
        elements = [name.strip() for name in f.readlines()]
    result = collections.OrderedDict()
    used_symbols = set()

    for name in elements:
        proposals = symbols_sorted_by_score(name)
        for p in proposals:
            if p not in used_symbols:
                result[name] = p
                used_symbols.add(p)
                break
        else:
            result[name] = None
    return result

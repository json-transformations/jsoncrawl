"""Tree Crawler Tests."""
from copy import deepcopy

from jsoncrawl.core import Node, node_visitor

FORECAST_MAPPING = {
    "city": "Timbuktu",
    "date": "2017-09-28",
    "coord": {"lat": 16.7735, "lon": -3.0074}
}
FORECAST_MAPPING_KEYS = [
    '',
    'city',
    'coord',
    'coord.lat',
    'coord.lon',
    'date'
]

FORECAST_SEQUENCE = [
    {"day": "Monday", "temp": {"hi": 105, "low": 81}},
    {"day": "Tuesday", "temp": {"hi": 109, "low": 81}}
]
FORECAST_SEQUENCE_KEYS = [
    '',
    '0',
    '0.day',
    '0.temp',
    '0.temp.hi',
    '0.temp.low',
    '1',
    '1.day',
    '1.temp',
    '1.temp.hi',
    '1.temp.low'
]
FORECAST_SEQUENCE_KEYS_WITH_WILDCARD = [
    '',
    '*',
    '*.day',
    '*.temp',
    '*.temp.hi',
    '*.temp.low'
]

FORECAST = deepcopy(FORECAST_MAPPING)
FORECAST.update({"forecast": FORECAST_SEQUENCE})
FORECAST_KEYS = [
    '',
    'city',
    'coord',
    'coord.lat',
    'coord.lon',
    'date',
    'forecast',
    'forecast.*',
    'forecast.*.day',
    'forecast.*.temp',
    'forecast.*.temp.hi',
    'forecast.*.temp.low'
]

TEST_DATA = {'k1': {'k2': 'v2', 'k3': ['i1']}}
RAW_OUTPUT = [
    Node(keys=[], val={'k1': {'k2': 'v2', 'k3': ['i1']}}, dtype='object'),
    Node(keys=['k1'], val={'k2': 'v2', 'k3': ['i1']}, dtype='object'),
    Node(keys=['k1', 'k2'], val='v2', dtype='string'),
    Node(keys=['k1', 'k3'], val=['i1'], dtype='array')
]


def get_keys(node):
    return '.'.join(map(str, node.keys))


def test_treecrawler_raw_output():
    """Outputs a list of tuples.
    1st element is the parent node.
    2nd elemeent is a list of child nodes.
    """
    result = node_visitor(TEST_DATA, lambda x: x)
    assert sorted(result) == RAW_OUTPUT


def test_treecrawler_primitive():
    assert sorted(set(node_visitor('', get_keys))) == ['']


def test_treecrawler_primitive():
    assert sorted(set(node_visitor('', get_keys, objects=False))) == ['']


def test_treecrawler_mapping():
    result = set(node_visitor(FORECAST_MAPPING, get_keys, arrays=True))
    assert sorted(result) ==  FORECAST_MAPPING_KEYS


def test_treecrawler_sequence():
    result = set(node_visitor(FORECAST_SEQUENCE, get_keys, arrays=True))
    assert sorted(result) == FORECAST_SEQUENCE_KEYS


def test_treecrawler_without_array_crawler():
    result = set(node_visitor(FORECAST, get_keys, arrays=False))
    assert sorted(result) == FORECAST_MAPPING_KEYS + ['forecast']


def test_treecrawler_with_element_char():
    result = set(node_visitor(FORECAST_SEQUENCE, get_keys, element_ch='*'))
    assert sorted(result) == FORECAST_SEQUENCE_KEYS_WITH_WILDCARD


def test_treecrawler():
    result = set(node_visitor(FORECAST, get_keys, element_ch='*'))
    assert sorted(result) == FORECAST_KEYS

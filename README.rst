JSON Tree Crawler
=================

|Build Status| |Coverage Status|

*JSON node crawler; traverse JSON trees; visit each node; yield results*.

Installation
------------

.. code-block::

    pip install jsoncrawl

Description
-----------

*JSON node visitor*.

Yields results of a user provided `process_node` funct.

The `process node` function accepts Nodes; Nodes are 3-D named tuples:
    1. The node's path; a list of JSON object keys/indexes.
    2. The node's value.
    3. The node's JSON data type (i.e. object, array, string, number, etc.)

Options:
    * Option to crawl through JSON objects.
    * Option to crawl through JSON arrays.
    * Option to use wildcard characters to substitute for index numbers.

Usage
-----

.. code-block:: python

    def node_visitor(d, process_node, objects=True, arrays=False, element_ch=None):
        """Call process_node funct for every node in tree and yield results."""

d (obj):
    Data to traverse (the tree)

process_node (funct):
    Accepts a Node as an argument.
    Example: `lambda node: '.'.join(map(str, node.keys))`

objects (bool):
    Visit the items in an object?

arrays (bool):
    Visit the elements in arrays? Automatically set if `element_ch`.

element_char (str):
    Replaces sequence index numbers with this character when set;
    if not visit_arrays then ignore this option.

How it Works
------------

.. code-block:: python

        first_node = Node(keys=[], val=d, dtype=get_type(d))
        to_crawl = deque([first_node])
        while to_crawl:
            node = to_crawl.popleft()
            yield process_node(node)
            children = get_children(node, element_ch, objects, arrays)
            to_crawl.extend(children)

Example
-------

.. code-block:: python

    """Print a list of unique keys in a JSON document.""

    from jsoncrawl import node_visitor

    def process_node(node):
        return '.'.join(map(str, node.keys))

    data = {'key1': 'test1', {'key2': 'test2'}}
    for unique_key in set(node_visitor(data, process_node, element_ch='*')):
        print(unique_key)

.. |Build Status| image:: https://travis-ci.org/json-transformations/jsoncrawl.svg?branch=master
   :target: https://travis-ci.org/json-transformations/jsoncrawl
.. |Coverage Status| image:: https://coveralls.io/repos/github/json-transformations/jsoncrawl/badge.svg?branch=master
   :target: https://coveralls.io/github/json-transformations/jsoncrawl?branch=master

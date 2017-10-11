jsoncrawl
=========

JSON node crawler; traverse JSON trees; visit each node; yield results.

Installation
------------

`pip install jsoncrawl`

Usage
-----

.. code::

    def node_visitor(d, process_node, objects=True, arrays=False, element_ch=None):
        """Call process_node funct for every node in tree and yield results.

        d (obj):
            Data to traverse (the tree)

        process_node (funct):
            Accepts a parent Node and list of child Nodes as args. Example:
            lambda parent, children: '.'.join(map(str, parent.keys))

        objects (bool):
            Visit the items in an object?

        arrays (bool):
            Visit the elements in arrays? Automatically set if `element_ch`.

        element_char (str):
            Replaces sequence index numbers with this character when set;
            if not visit_arrays then ignore this option.
        """

#!/usr/bin/env python

# $Id: test_pseudoxml.py 8481 2020-01-31 08:17:24Z milde $
# Author: Lea Wiemann <LeWiemann@gmail.com>
# Copyright: This module has been placed in the public domain.

"""
Test for pseudo-XML writer.
"""
from __future__ import absolute_import

if __name__ == '__main__':
    import __init__
from test_writers import DocutilsTestSupport


def suite():
    s = DocutilsTestSupport.PublishTestSuite('pseudoxml')
    s.generateTests(totest)
    return s

totest = {}

totest['basic'] = [
# input
["""\
This is a paragraph.

----------

This is another paragraph.

A Section
---------

Foo.
""",
# output
"""\
<document source="<string>">
    <paragraph>
        This is a paragraph.
    <transition>
    <paragraph>
        This is another paragraph.
    <section ids="a-section" names="a\\ section">
        <title>
            A Section
        <paragraph>
            Foo.
"""]
]

if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')

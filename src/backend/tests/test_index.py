#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import unittest
import tempfile
import shutil
from indexstore import IndexStore

class TestIndex(unittest.TestCase):

    def setUp(self):
        self.data_dir = tempfile.mkdtemp()
        self.index = IndexStore(self.data_dir)
        self.index._connect()

    def tearDown(self):
        self.index._disconnect()
        shutil.rmtree(self.data_dir)

    def test_add(self):
        print self.index.add("title", "Body of text")


if __name__ == '__main__':
    unittest.main()

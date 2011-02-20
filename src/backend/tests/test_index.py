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
        self.assertEqual(self.index.add("title", "Body of text"), '0')
        self.assertEqual(self.index.add("title2", "Body of text",
                                        date='2010-01-10'), '1')
        self.assertEqual(self.index.add("title3", "Lots of text",
                                        category='general'), '2')

    def test_search(self):
        self.index.add("title", "Body of text")
        self.index._conn.flush()
        res = self.index.search("Body")
        self.assertEquals(len(res), 1)
        self.assertEquals(res[0].rank, 0)
        self.assertEquals(res[0].id, '0')
        
    def test_search_two(self):
        self.index.add("title", "Body of text")
        self.index.add("title2", "Lot of text", date='2010-02-10')
        self.index._conn.flush()
        res = self.index.search("text")
        self.assertEquals(len(res), 2)
        self.assertEquals(res[0].id, '0')
        self.assertEquals(res[1].id, '1')

    def test_search_category(self):
        self.index.add("title", "Body of text")
        self.index.add("title2", "Example text general")
        self.index.add("title3", "Lots of text", category='general')
        self.index._conn.flush()
        res = self.index.search('lots')
        self.assertEquals(len(res), 1)
        res = self.index.search('lots', category='general')
        self.assertEquals(len(res), 1)
        res = self.index.search('nothing', category='general')
        self.assertEquals(len(res), 0)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import unittest
import tempfile
import shutil
from toc import TOC, TOCEntry

class TestTOC(unittest.TestCase):

    def setUp(self):
        self.data_dir = tempfile.mkdtemp()
        self.toc = TOC(self.data_dir)
        self.toc._connect()
        self.data = TOCEntry('http://www.example.com', 0)

    def tearDown(self):
        self.toc._disconnect()
        shutil.rmtree(self.data_dir)
    
    def test_add_one(self):
        self.toc.add(self.data)
        self.assertEquals(self.toc._count(), 1)

    def test_add_many(self):
        data = [
            self.data,
            TOCEntry('http://www.example1.com', 1)
        ]
        self.toc.add(data)
        self.assertEquals(self.toc._count(), 2)
        
    def test_get_not_exists(self):
        self.assertIsNone(self.toc.get(1))

    def test_get_success(self):
        self.toc.add(self.data)
        res = self.toc.get(1)
        self.assertEquals(res.url, self.data.url)

    def test_get_invalid_input(self):
        self.assertIsNone(self.toc.get('1'))

    def test_exists_true(self):
        self.toc.add(self.data)
        self.assertTrue(self.toc.exists(self.data.url))
        self.assertFalse(self.toc.exists("nourl"))


if __name__ == '__main__':
    unittest.main()

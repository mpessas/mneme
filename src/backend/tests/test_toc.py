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

    def tearDown(self):
        shutil.rmtree(self.data_dir)
    
    def test_add_one(self):
        with self.toc.connect():
            data = TOCEntry('http://www.example.com', 0)
            self.toc.add(data)
            self.assertEquals(self.toc._count(), 1)

    def test_add_many(self):
        with self.toc.connect():
            data = [
                TOCEntry('http://www.example.com', 0),
                TOCEntry('http://www.example1.com', 1)
            ]
            self.toc.add(data)
            self.assertEquals(self.toc._count(), 2)


if __name__ == '__main__':
    unittest.main()

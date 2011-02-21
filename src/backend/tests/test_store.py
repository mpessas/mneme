#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import tempfile
import unittest
import shutil
from datastore import DataStore

class TestStore(unittest.TestCase):

    def setUp(self):
        self.data_dir = tempfile.mkdtemp()
        self.store = DataStore(self.data_dir)
        self.urls = [
            'http://example.com',
            'http://example.org',
        ]
        self.text = [
            u'Example text for the first url',
            u'Δοκιμαστικό κείμενο για δεύτερο url',
        ]
        self.categories = [
            ['cat1', ],
            ['cat1', 'cat2', ],
        ]

    def tearDown(self):
        shutil.rmtree(self.data_dir)

    def test_add(self):
        self.assertTrue(
            self.store.add(self.urls[0], self.text[0], self.categories[0])
        )

    def test_search(self):
        for i in xrange(len(self.urls)):
            self.store.add(self.urls[i], self.text[i], self.categories[i])
        


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import unittest
from document import Document


class TestDocument(unittest.TestCase):

    def test_correct_url(self):
        doc = Document("http://www.example.com")
        self.assertIsNotNone(doc.get_text())


if __name__ == '__main__':
    unittest.main()

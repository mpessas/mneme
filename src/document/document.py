# -*- coding: utf-8 -*-

import urllib2

class Document(object):
    """A document to be indexed."""

    def __init__(self, url):
        self.document = urllib2.urlopen(url)

    def get_text(self):
        return self.document.read()

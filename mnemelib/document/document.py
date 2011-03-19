# -*- coding: utf-8 -*-

import urllib
import lxml.html


class Document(object):
    """A document to be indexed."""

    def __init__(self, url):
        f = urllib.urlopen(url)
        self.document = lxml.html.document_fromstring(f.read())

    def get_text(self):
        """Return the text from an html document."""
        return self.document.text_content()

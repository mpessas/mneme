# -*- coding: utf-8 -*-

import lxml.html

class Document(object):
    """A document to be indexed."""

    def __init__(self, url):
        self.document = lxml.html.parse(url).getroot()

    def get_text(self):
        return self.document.text_content()

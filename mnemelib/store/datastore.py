# -*- coding: utf-8 -*-

import os
from indexstore import IndexStore


class DataStore(object):
    """Class to save/retrieve data from datastore.

    Uses xapian for indexing the data.
    """

    def __init__(self, data_dir):
        if not os.path.exists(data_dir):
            os.mkdir(data_dir)
        self.index = IndexStore(data_dir)

    def add(self, url, text, categories=[]):
        """Add an entry to the datastore."""
        with self.index.connect():
            self.index.add(url, text, categories)

    def search(self, text, category=None):
        """Search for matching documents for a term
        among the indexed documents.
        """
        res = self.index.search(text, category)
        return (self.index.get_url(r) for r in res)

    def exists(self, url):
        """Check whether a URL has already been indexed."""
        self.index.exists(url)

    def get_categories(self):
        """Get a list of the categories defined in the index."""
        return self.index.get_categories()

    def get_urls(self):
        """Get a list of the urls in the index."""
        return self.index.get_urls()

    def get_entries(self):
        """Get a list of the entries in the index."""
        docs = self.index.get_documents()
        return ((d.data['url'][0], d.data['category']) for d in docs)

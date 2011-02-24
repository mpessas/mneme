# -*- coding: utf-8 -*-

import os
import os.path
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
        with self.index.connect():
            self.index.add(url, text, categories)

    def search(self, text, category=None):
        res = self.index.search(text, category)
        return (self.index.get_url(r) for r in res)

    def exists(self, url):
        self.index.exists(url)

    def get_categories(self):
        return self.index.get_categories()

    def get_urls(self):
        return self.index.get_urls()
        
    

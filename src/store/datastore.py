# -*- coding: utf-8 -*-

import os
import os.path
from indexstore import IndexStore

class DataStore(object):
    """
    Class to save/retrieve data from datastore.
    
    Uses xapian for indexing the data.
    """

    def __init__(self, data_dir=None):
        self._data_dir = data_dir
        if self._data_dir is None:
            self._data_dir = os.path.expanduser(u'~/.saveurl/')
        if not os.path.exists(self._data_dir):
            os.mkdir(self._data_dir)
        self.index = IndexStore(self._data_dir)

    def add(self, url, text, categories=[]):
        with self.index.connect():
            self.index.add(url, text, categories)

    def search(self, text, category=None):
        res = self.index.search(text, category)
        return (self.index.get_url(r) for r in res)
        
    

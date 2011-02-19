# -*- coding: utf-8 -*-

import os.path

class Data(object):
    """
    Class to save/retrieve data from datastore.
    
    Uses xapian for indexing the data and an sqlite database
    to save the indexed urls.
    """

    def __init__(self):
        self._sqlitedb = u'~/.saveurls/urls.db'
        if not os.path.exists(self._sqlitedb):
            self._init_backend()

    def _init_backend(self):
        """Initialize the backend.
        
        The backend consists of a sqlite database serving as TOC and
        a xapian database for indexing the urls.
        """
        self._init_sql()
        self._init_xapian()

    def _init_sql(self):
        """Initialize the sql table."""
        pass

    def _init_xapian(self):
        """Initialize the xapian backend."""
        pass
        
        
    

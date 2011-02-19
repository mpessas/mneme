# -*- coding: utf-8 -*-

import os
import os.path
import sqlite3

class Data(object):
    """
    Class to save/retrieve data from datastore.
    
    Uses xapian for indexing the data and an sqlite database
    to save the indexed urls.
    """

    def __init__(self):
        self._data_dir = os.path.expanduser(u'~/.saveurl/')
        print self._data_dir
        self._sqlitedb_path = os.path.join(self._data_dir, u'urls.db')
        if not os.path.exists(self._data_dir):
            os.mkdir(self._data_dir)
        if not os.path.exists(self._sqlitedb_path):
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
        self._conn = sqlite3.connect(self._sqlitedb_path)
        c = self._conn.cursor()
        query = "CREATE TABLE urls (id INTEGER PRIMARY KEY AUTOINCREMENT," + \
                "url TEXT NOT NULL UNIQUE," + \
                "xapian_id INTEGER NOT NULL UNIQUE)"
        
        c.execute(query)
        self._conn.commit()
        c.close()
        self._conn.close()

    def _init_xapian(self):
        """Initialize the xapian backend."""
        pass
        
        
    

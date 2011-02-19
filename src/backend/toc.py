# -*- coding: utf-8 -*-

import os.path
import sqlite3
import collections
from contextlib import contextmanager


class TOC(object):
    """Class to serve as a Table Of Contents for the indexed urls."""

    def __init__(self, data_dir):
        self._cols = ('id', 'url', 'xapian_id')
        self._sqlitedb_path = os.path.join(data_dir, u'urls.db')
        if not os.path.exists(self._sqlitedb_path):
            self._create_table()

    def _create_table(self):
        """Initialize the table of contents."""
        with self.connect():
            query = """CREATE TABLE urls (
                    %s INTEGER PRIMARY KEY AUTOINCREMENT,
                    %s TEXT NOT NULL UNIQUE,
                    %s INTEGER NOT NULL UNIQUE)""" % self._cols
            self._conn.execute(query)

    def _connect(self):
        self._conn = sqlite3.connect(self._sqlitedb_path)

    def _disconnect(self):
        self._conn.close()

    @contextmanager
    def connect(self):
        self._connect()
        yield
        self._disconnect()

    def _add(self, data):
        with self._conn:
            query = "INSERT INTO urls (%s, %s) VALUES (?, ?)" % (self._cols[1],
                                                                 self._cols[2])
            self._conn.execute(query, (data.url, data.xapian_id))
        
    def add(self, data):
        """Add an entry to the TOC.

        One can add many entries if an iterable is provided.
        """
        if isinstance(data, collections.Iterable):
            map(self._add, data)
        else:
            self._add(data)

    def _count(self):
        c = self._conn.cursor()
        c.execute("SELECT COUNT(*) FROM urls")
        n = c.fetchone()[0]
        c.close()
        return n

    def get(self, toc_id):
        query = "SELECT * FROM urls WHERE %s = ?" % self._cols[0]
        c = self._conn.cursor()
        c.execute(query, (toc_id, ))
        res = c.fetchone()
        if res is None:
            return None
        entry = TOCEntry(res[1], res[2], res[0])
        c.close()
        return entry


class TOCEntry(object):
    """An entry in the TOC."""

    def __init__(self, url, xapian_id, toc_id=None):
        self.toc_id = toc_id
        self._url = url
        self._xapian_id = xapian_id

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    @property
    def xapian_id(self):
        return self._xapian_id

    @xapian_id.setter
    def xapian_id(self, value):
        self._xapian_id = value

# -*- coding: utf-8 -*-

import os.path
import datetime
from contextlib import contextmanager
import xappy

class IndexStore(object):
    """Class to access the index for the urls."""

    def __init__(self, data_dir):
        self._xapiandb_path = os.path.join(data_dir, u'index.db')
        if not os.path.exists(self._xapiandb_path):
            self._setup_index()

    def _setup_index(self):
        with self.connect():
            self._conn.add_field_action(
                'title', xappy.FieldActions.INDEX_FREETEXT,
                weight=5, language='en'
            )
            self._conn.add_field_action(
                'text', xappy.FieldActions.INDEX_FREETEXT,
                language='en', spell=True, nopos=True
            )
            self._conn.add_field_action(
                'date', xappy.FieldActions.SORTABLE,
                type='date'
            )

    def _connect(self):
        self._conn = xappy.IndexerConnection(self._xapiandb_path)

    def _disconnect(self):
        self._conn.flush()
        self._conn.close()

    @contextmanager
    def connect(self):
        self._connect()
        yield
        self._disconnect()

    def add(self, title, text, date=datetime.date.today()):
        doc = xappy.UnprocessedDocument()
        doc.fields.append(xappy.Field('title', title))
        doc.fields.append(xappy.Field('text', text))
        doc.fields.append(xappy.Field('date', date))
        return self._conn.add(doc)

    def search(self, text):
        conn = xappy.SearchConnection(self._xapiandb_path)
        q = conn.query_field('text', text)
        return conn.search(q, 0, 10)

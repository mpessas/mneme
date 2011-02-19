# -*- coding: utf-8 -*-

import os.path
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
                'url', xappy.FieldActions.INDEX_FREETEXT,
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
            self._conn.add_field_action(
                'tag', xappy.FieldActions.FACET
            )

    def _connect(self):
        self._conn = xappy.IndexerConnection(self._xapiandb_path)

    def _disconnect(self):
        self._conn.close()

    @contextmanager
    def connect(self):
        self._connect()
        yield
        self._disconnect()
        

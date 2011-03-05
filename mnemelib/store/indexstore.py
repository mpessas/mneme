# -*- coding: utf-8 -*-

import os.path
import datetime
from contextlib import contextmanager
import xappy


class IndexStore(object):
    """Class to access the index for the urls."""

    def __init__(self, data_dir):
        self.schema_version = '0.1'
        self._xapiandb_path = os.path.join(data_dir, u'index.db')
        if not os.path.exists(self._xapiandb_path):
            self._setup_index()

    def _setup_index(self):
        with self.connect():
            self._conn.add_field_action(
                'url', xappy.FieldActions.INDEX_EXACT
            )
            self._conn.add_field_action(
                'url', xappy.FieldActions.STORE_CONTENT
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
                'date', xappy.FieldActions.STORE_CONTENT
            )
            self._conn.add_field_action(
                'category', xappy.FieldActions.INDEX_EXACT
            )
            self._conn.add_field_action(
                'category', xappy.FieldActions.STORE_CONTENT
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

    def add(self, url, text, categories=[], date=datetime.date.today()):
        doc = xappy.UnprocessedDocument()
        doc.fields.append(xappy.Field('url', url))
        doc.fields.append(xappy.Field('text', text))
        for cat in categories:
            doc.fields.append(xappy.Field('category', cat))
        doc.fields.append(xappy.Field('date', str(date)))
        return self._conn.add(doc)

    def search(self, text, category=None):
        conn = xappy.SearchConnection(self._xapiandb_path)
        q = conn.query_field('text', text)
        if category:
            facet_q = conn.query_facet('category', category)
            q = conn.query_filter(q, facet_q)
        return conn.search(q, 0, 10)

    def get_categories(self):
        conn = xappy.SearchConnection(self._xapiandb_path)
        return conn.iter_terms_for_field('category')

    def get_urls(self):
        conn = xappy.SearchConnection(self._xapiandb_path)
        return conn.iter_terms_for_field('url')

    def get_url(self, search_result):
        return search_result.data['url'][0]

    def exists(self, url):
        conn = xappy.SearchConnection(self._xapiandb_path)
        q = conn.query_field('url', url)
        res = conn.search(q, 0, 1)
        assert len(res) == 1 or len(res) == 0
        return len(res) == 1

    def get_documents(self):
        conn = xappy.SearchConnection(self._xapiandb_path)
        return conn.iter_documents()

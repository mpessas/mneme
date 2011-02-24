#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import argparse
import json
import document
import store
import settings


def add_url(args):
    """Adds the given URL to the index."""
    doc = document.Document(args.url)
    index = store.DataStore(settings.DATA_DIR)
    index.add(args.url, doc.get_text(), args.category)


def search_terms(args):
    """Prints the URLs that matched the terms supplied in the command line."""
    index = store.DataStore(settings.DATA_DIR)
    for res in index.search(' '.join(args.terms), args.category):
        print res


def list_categories(args):
    """List the categories defined in the index."""
    index = store.DataStore(settings.DATA_DIR)
    for cat in index.get_categories():
        print cat


def list_urls(args):
    """List the categories defined in the index."""
    index = store.DataStore(settings.DATA_DIR)
    for url in index.get_urls():
        print url


def export_data(args):
    index = store.DataStore(settings.DATA_DIR)
    json.dump(
        [entry for entry in index.get_entries()],
        args.outfile,
        indent=4
    )
    args.outfile.close()


def parse_args():
    """Handle arguments."""
    parser = argparse.ArgumentParser(
        description=u'Index the content of a URL for future reference.'
    )
    subparsers = parser.add_subparsers(
        title=u'subcommands', description=u'Available commands'
    )

    add_parser = subparsers.add_parser('add', help=u'Add a URL to the index.')
    add_parser.add_argument('url', help=u'The URL to add to the index.')
    add_parser.add_argument(
        '-c', '--category', action='append',
        help=u'A category this URL belongs to.'
    )
    add_parser.set_defaults(func=add_url)

    search_parser = subparsers.add_parser(
        'search', help=u'Search the index for a term.'
    )
    search_parser.add_argument(
        'terms', nargs='+', help=u'A list of terms to search for.'
    )
    search_parser.add_argument(
        '-c', '--category', help=u'Category the URl must match.'
    )
    search_parser.set_defaults(func=search_terms)

    list_categories_parser = subparsers.add_parser(
        'list_categories', help=u'List the defined categories.'
    )
    list_categories_parser.set_defaults(func=list_categories)

    list_urls_parser = subparsers.add_parser(
        'list_urls', help=u'List the indexed urls.'
    )
    list_urls_parser.set_defaults(func=list_urls)

    export_parser = subparsers.add_parser(
        'export', help=u'Export data in index.'
    )
    export_parser.add_argument('outfile', type=argparse.FileType('w'))
    export_parser.set_defaults(func=export_data)

    return parser.parse_args()


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    args = parse_args()
    args.func(args)


if __name__ == '__main__':
    sys.exit(main())

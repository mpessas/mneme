#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import argparse


def add_url(args):
    """Adds the given URL to the index."""
    print args.url


def search_terms(args):
    """Prints the URLs that matched the terms supplied in the command line."""
    print ' '.join(args.terms)


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
    add_parser.set_defaults(func=add_url)

    search_parser = subparsers.add_parser(
        'search', help=u'Search the index for a term.'
    )
    search_parser.add_argument(
        'terms', nargs='+', help=u'A list of terms to search for.'
    )
    search_parser.set_defaults(func=search_terms)

    return parser.parse_args()


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    args = parse_args()
    args.func(args)


if __name__ == '__main__':
    sys.exit(main())

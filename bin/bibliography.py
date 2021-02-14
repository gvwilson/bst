#!/usr/bin/env python

'''Check consistency of bibliography definitions and references.'''

import argparse
import re
import sys

import utils


# Citation use Jekyll inclusions.
CITATION = re.compile(r'\{%\s+include\s+cite\b.+?key="(.+?)".+?%\}', re.DOTALL)

# Definitions are left-justified starting with an upper-case letter.
DEFINITION = re.compile(r'^([A-Z][A-Za-z0-9]+)$', re.DOTALL + re.MULTILINE)

def main():
    '''Main driver.'''
    options = get_options()
    defined = get_definitions(options.bibliography)
    cited = get_citations(options.sources)
    utils.report('bibliography', cited=cited, defined=defined)


def get_options():
    '''Get command-line options.'''
    parser = argparse.ArgumentParser()
    parser.add_argument('--bibliography', help='Path to bibliography Markdown.')
    parser.add_argument('--sources', nargs='+', help='List of input files')
    return parser.parse_args()


def get_citations(filenames):
    '''Create set of citations in source files.'''
    result = set()
    for filename in filenames:
        with open(filename, 'r') as reader:
            text = reader.read()
            for match in CITATION.finditer(text):
                for key in match.group(1).split(','):
                    result.add(key.strip())
    return result


def get_definitions(filename):
    '''Create set of citation keys.'''
    result = set()
    with open(filename, 'r') as reader:
        text = reader.read()
        for match in DEFINITION.finditer(text):
            result.add(match.group(1))
    return result


if __name__ == '__main__':
    main()

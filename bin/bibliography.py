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
    options = utils.get_options(
        ['--bibliography', False, 'Path to bibliography Markdown'],
        ['--sources', True, 'List of input files']
    )
    defined = get_definitions(options.bibliography)
    cited = utils.get_all_matches(CITATION, options.sources)
    utils.report('bibliography', cited=cited, defined=defined)


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

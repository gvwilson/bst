#!/usr/bin/env python

'''Check consistency of bibliography definitions and references.'''

import argparse
import re
import sys

import utils


# Citation use <cite>key,key</cite>.
CITATION = re.compile(r'<cite>(.+?)</cite>', re.DOTALL)

# Definitions are left-justified starting with an upper-case letter.
DEFINITION = re.compile(r'^([A-Z][A-Za-z0-9]+)$', re.DOTALL + re.MULTILINE)

def bibliography(options):
    '''Main driver.'''
    defined = get_definitions(options.bibliography)
    cited = utils.get_all_matches(CITATION, options.sources)
    utils.report('bibliography', cited=cited, defined=defined)


def get_definitions(filename):
    '''Create set of citation keys.'''
    result = set()
    text = utils.read_file(filename)
    for match in DEFINITION.finditer(text):
        result.add(match.group(1))
    return result


if __name__ == '__main__':
    options = utils.get_options(
        ['--bibliography', False, 'Path to bibliography Markdown'],
        ['--sources', True, 'List of input files']
    )
    bibliography(options)

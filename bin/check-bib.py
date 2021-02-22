#!/usr/bin/env python

'''Check consistency of bibliography definitions and references.'''

import argparse
import re
import sys

import utils


# Citation use <cite>key,key</cite>.
CITATION = re.compile(r'<cite>(.+?)</cite>', re.DOTALL)

def check_bib(options):
    '''Main driver.'''
    defined = get_definitions(options.bibliography)
    cited = utils.get_all_matches(CITATION, options.sources)
    utils.report('bibliography', cited=cited, defined=defined)


def get_definitions(filename):
    '''Create set of citation keys.'''
    raw = utils.read_yaml(filename)
    return set([entry['key'] for entry in raw])


if __name__ == '__main__':
    options = utils.get_options(
        ['--bibliography', False, 'Path to bibliography YAML file'],
        ['--sources', True, 'List of input files']
    )
    check_bib(options)

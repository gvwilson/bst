#!/usr/bin/env python

'''Check consistency of glossary definitions and references.'''

import re
import sys

import utils


# Cross-references look like internal links.
CROSS_REF = re.compile(r'\[.+?\]\((#.+?)\)', re.DOTALL)


def check_gloss(options):
    '''Main driver.'''
    glossary = utils.read_yaml(options.glossary)
    check_order(glossary)
    defined = get_definitions(glossary)
    referenced = utils.get_all_matches(utils.GLOSS_REF, options.sources, no_duplicates=True) | get_internal(glossary)
    utils.report('glossary', referenced=referenced, defined=defined)


def check_order(glossary):
    '''Check that entries are in alphabetical order.'''
    previous = None
    unordered = []
    for entry in glossary:
        if previous is not None:
            if entry['term'].lower() < previous['term'].lower():
                unordered.append(entry['term'])
        previous = entry
    if unordered:
        print('- glossary')
        print('  - out of order')
        for item in unordered:
            print(f'    - {item}')


def get_internal(glossary):
    '''Create set of internal references within glossary definitions.'''
    result = set()
    for entry in glossary:
        for match in CROSS_REF.finditer(entry['def']):
            result.add(match.group(1))
    return result


def get_definitions(glossary):
    '''Create set of keys in glossary.'''
    return {entry['key'] for entry in glossary}


if __name__ == '__main__':
    options = utils.get_options(
        ['--glossary', False, 'Path to glossary YAML file'],
        ['--sources', True, 'List of input files']
    )
    check_gloss(options)

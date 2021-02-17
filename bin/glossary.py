#!/usr/bin/env python

'''Check consistency of glossary definitions and references.'''

import re
import sys

import utils


# Cross-references look like internal links.
CROSS_REF = re.compile(r'\[.+?\]\((#.+?)\)', re.DOTALL)

# Glossary references use <g key="...">...</g>.
GLOSS_REF = re.compile(r'<g\s+key="(.+?)">', re.DOTALL)


def glossary(options):
    '''Main driver.'''
    glossary = utils.read_yaml(options.glossary)
    defined = get_definitions(glossary)
    referenced = utils.get_all_matches(GLOSS_REF, options.sources) | get_internal(glossary)
    utils.report('glossary', referenced=referenced, defined=defined)


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
    glossary(options)

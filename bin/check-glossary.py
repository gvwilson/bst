#!/usr/bin/env python

import argparse
import re
import sys

import utils


# Cross-references look like internal links.
CROSS_REF = re.compile(r'\[.+?\]\((#.+?)\)', re.DOTALL)

# Glossary references use Jekyll inclusions.
GLOSS_REF = re.compile(r'\{%\s+include\s+gloss\b.+?key="(.+?)".+?%\}', re.DOTALL)


def main():
    '''Main driver.'''
    options = get_options()
    glossary = utils.read_yaml(options.glossary)
    defined = get_definitions(glossary)
    referenced = get_references(options.sources) | get_internal(glossary)
    utils.report('Referenced but not defined', referenced - defined)
    utils.report('Defined but not referenced', defined - referenced)


def get_options():
    '''Get command-line options.'''
    parser = argparse.ArgumentParser()
    parser.add_argument('--glossary', help='Path to glossary YAML file.')
    parser.add_argument('--sources', nargs='+', help='List of input files')
    return parser.parse_args()


def get_references(filenames):
    '''Create set of glossary references in source files.'''
    result = set()
    for filename in filenames:
        with open(filename, 'r') as reader:
            text = reader.read()
            for match in GLOSS_REF.finditer(text):
                result.add(match.group(1))
    return result


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
    main()

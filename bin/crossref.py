#!/usr/bin/env python

'''Check chapter cross-references.'''

import argparse
import re
import sys

import utils


# Chapter and appendix references use <chap key="..."></chap> and <app key="..."></app>.
CHAP_REF = re.compile(r'<(chap|app)\s+key="(.+?)">', re.DOTALL)


def crossref(options):
    '''Main driver.'''
    config = utils.read_yaml(options.config)
    defined = get_slugs(config)
    referenced = utils.get_all_matches(CHAP_REF, options.sources, group=2)
    utils.report('cross-references', checkOnlyRight=False, referenced=referenced, defined=defined)


def get_slugs(config):
    '''Create set of chapter slugs found in configuration.'''
    return {entry['slug'] for entry in config['chapters'] if 'slug' in entry}


if __name__ == '__main__':
    options = utils.get_options(
        ['--config', False, 'Path to YAML configuration file'],
        ['--sources', True, 'List of input files']
    )
    crossref(options)

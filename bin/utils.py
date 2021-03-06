import argparse
import re
import sys
import yaml

'''Utilities used across all tools.'''


# Glossary references use <span g="...">...</span>.
GLOSS_REF = re.compile(r'<span\s+g="(.+?)">', re.DOTALL)

# Raw Jekyll blocks.
RAW = re.compile(r'{%\s+raw\s+%}.*?{%\s+endraw\s+%}', re.DOTALL)


def get_all_matches(pattern, filenames, group=1, scrub=True, no_duplicates=False):
    '''Create set of matches in source files.'''
    result = set()
    for filename in filenames:
        result = result | get_matches(pattern, filename, group, scrub, no_duplicates)
    return result


def get_matches(pattern, filename, group=1, scrub=True, no_duplicates=False):
    '''Get matches from a single file.'''
    result = set()
    text = read_file(filename, scrub)
    for match in pattern.finditer(text):
        for key in match.group(group).split(','):
            if no_duplicates and (key in result):
                print(f'** duplicate key "{key}"', file=sys.stderr)
            result.add(key.strip())
    return result


def get_options(*options):
    '''Get command-line options.'''
    parser = argparse.ArgumentParser()
    for [flag, nargs, explain] in options:
        if nargs:
            parser.add_argument(flag, nargs='+', help=explain)
        else:
            parser.add_argument(flag, help=explain)
    return parser.parse_args()


def get_slugs_and_paths(config):
    '''Return list of [slug, filename] pairs for all chapters.'''
    result = []
    for entry in config['chapters']:
        if 'slug' not in entry:
            continue
        if 'file' in entry:
            result.append([entry['slug'], entry['file']])
        else:
            result.append([entry['slug'], f'./{entry["slug"]}/index.md'])
    return result


def read_file(filename, scrub=True):
    '''Read a file, removing raw sections if requested.'''
    with open(filename, 'r') as reader:
        text = reader.read()
        if scrub:
            text = RAW.sub('', text)
        return text


def read_yaml(filename):
    '''Load and return a YAML file.'''
    with open(filename, 'r') as reader:
        return yaml.load(reader, Loader=yaml.FullLoader)


def report(title, checkOnlyRight=True, **kwargs):
    '''Report items if present.'''
    assert len(kwargs) == 2, 'Must have two sets to report'
    left, right = kwargs.keys()
    onlyLeft = kwargs[left] - kwargs[right]
    onlyRight = kwargs[right] - kwargs[left]
    if onlyLeft or (checkOnlyRight and onlyRight):
        print(f'- {title}')
        if onlyLeft:
            print(f'  - {left} but not {right}')
            for item in sorted(onlyLeft):
                print(f'    - {item}')
        if checkOnlyRight and onlyRight:
            print(f'  - {right} but not {left}')
            for item in sorted(onlyRight):
                print(f'    - {item}')


def write_yaml(filename, data):
    '''Save a YAML file.'''
    with open(filename, 'w') as writer:
        return yaml.dump(data, writer)

#!/usr/bin/env python

'''Convert YAML bibliography to Markdown.'''

import utils


# Top of page.
HEADER = '''---
---

<dl class="bibliography">
'''

# Bottom of page.
FOOTER = '''

</dl>
'''

# Start of entry.
ENTRY_START = '<dd>'

# End of entry.
ENTRY_END = '</dd>'



def make_bib(options):
    '''Main driver.'''
    data = utils.read_yaml(options.input)
    entries = []
    for entry in data:
        assert 'type' in entry, \
            'Entries must have "type"'
        assert entry['type'] in HANDLERS, \
            f'Unknown entry type {entry["type"]}'
        text = HANDLERS[entry['type']](entry)
        entries.append(text)
    entries = '\n'.join(entries)
    result = f'{HEADER}{entries}{FOOTER}'
    with open(options.output, 'w') as writer:
        writer.write(result)


def article(entry):
    '''Convert article.'''
    return '\n'.join([
        key(entry),
        ENTRY_START,
        credit(entry),
        title(entry, True),
        article_info(entry),
        ENTRY_END
    ])


def book(entry):
    '''Convert book.'''
    return '\n'.join([
        key(entry),
        ENTRY_START,
        credit(entry),
        title(entry, False),
        bookInfo(entry),
        ENTRY_END
    ])


def inproceedings(entry):
    '''Convert proceedings entry.'''
    return '\n'.join([
        key(entry),
        ENTRY_START,
        credit(entry),
        title(entry, True),
        proceedingsInfo(entry),
        ENTRY_END
    ])



def link(entry):
    '''Convert link.'''
    return '\n'.join([
        key(entry),
        ENTRY_START,
        credit(entry),
        title(entry, True),
        ENTRY_END
    ])


# Lookup table for entry handlers.
HANDLERS = {
    'article': article,
    'book': book,
    'inproceedings': inproceedings,
    'link': link
}


def article_info(entry):
    '''Generate article information.'''
    assert ('journal' in entry) and ('year' in entry), \
        f'Entry requires journal and year: {str(entry)}'
    details = ''
    if 'volume' in entry:
        details = f'{entry["volume"]}'
    if 'number' in entry:
        details = f'{details}({entry["number"]})'
    if details:
        details = f', {details}'
    doi = ''
    if 'doi' in entry:
        doi = f', <a href="https://doi.org/{entry["doi"]}">{entry["doi"]}</a>'
    return f'<em>{entry["journal"]}</em>{details}, {entry["year"]}{doi}.'


def bookInfo(entry):
    '''Generate book information.'''
    assert ('publisher' in entry) and ('year' in entry) and ('isbn' in entry), \
        'Entry requires publisher, year, and ISBN'
    return f'{entry["publisher"]}, {entry["year"]}, {entry["isbn"]}.'


def proceedingsInfo(entry):
    '''Generate proceedings entry information.'''
    assert ('booktitle' in entry) and ('doi' in entry), \
        'Entry requires booktitle and doi'
    doi = f'<a href="https://doi.org/{entry["doi"]}">{entry["doi"]}</a>'
    return f'<em>{entry["booktitle"]}</em>, {doi}.'


def credit(entry):
    '''Generate credit (author or editor).'''
    names = None
    suffix = ''
    if 'author' in entry:
        names = entry['author']
    elif 'editor' in entry:
        names = entry['editor']
        suffix = ' (eds.)'
    assert names is not None, \
        'Entry must have author or editor'
    if len(names) == 1:
        names = names[0]
    elif len(names) == 2:
        names = f'{names[0]} and {names[1]}'
    elif len(names) > 2:
        front = ', '.join(names[0:-1])
        names = f'{front}, and {names[-1]}'
    return f'{names}{suffix}:'


def key(entry):
    '''Generate bibliography key.'''
    assert 'key' in entry, \
        'Every entry must have key'
    return f'<dt id="{entry["key"].lower()}" class="bibliography">{entry["key"]}</dt>'


def title(entry, quote):
    '''Generate title (possibly linking and/or quoting).'''
    assert 'title' in entry, \
        'Every entry must have title'
    title = f'<a href="{entry["url"]}">{entry["title"]}</a>' if ('url' in entry) else entry["title"]
    if quote:
        title = f'"{title}"'
    else:
        title = f'<em>{title}</em>'
    return f'{title}.'


if __name__ == '__main__':
    options = utils.get_options(
        ['--input', False, 'Path to input YAML bibliography file'],
        ['--output', False, 'Path to output Markdown file']
    )
    make_bib(options)

#!/usr/bin/env python

'''Convert a set of HTML pages to a single LaTeX document.'''

import sys
from bs4 import BeautifulSoup, NavigableString, Tag

import utils


# Ignore these nodes and their children.
IGNORE = {
    'footer',
    'head',
    'nav'
}

# Do nothing with these nodes but get their children.
RECURSE_ONLY = {
    'body',
    '[document]',
    'header',
    'html',
    'main',
    'td',
    'th'
}


def html2tex(options):
    '''Main driver.'''
    config = utils.read_yaml(options.config)
    filenames = get_filenames(options.site, config)
    accum = []
    for f in filenames:
        convert_file(f, accum)
    result = ''.join(accum)
    display(options, result)


def get_filenames(site, config):
    '''Get names of input files from configuration data.'''
    return [f"{site}/{entry['slug']}/index.html"
            for entry in config['chapters']
            if 'slug' in entry]


def convert_file(filename, accum):
    '''Translate a file from HTML to LaTeX.'''
    with open(filename, 'r') as reader:
        text = reader.read()
        dom = BeautifulSoup(text, 'html.parser')
        convert(dom.html, accum, True)
    return accum


def convert(node, accum, doEscape):
    '''Convert portion of tree to LaTeX, collecting text in accum.'''

    # Pure text
    if isinstance(node, NavigableString):
        accum.append(escape(node.string, doEscape))

    # Not a tag
    elif not isinstance(node, Tag):
        pass

    # Nothing to see here...
    elif node.name in IGNORE:
        pass

    # Ignore this but do its children
    elif node.name in RECURSE_ONLY:
        convert_children(node, accum, doEscape)

    # a => hyperlink
    elif node.name == 'a':
        link = escape(node['href'], doEscape)
        temp = ''.join(convert_children(node, [], doEscape))
        accum.append(rf'\hreffoot{{{temp}}}{{{link}}}')

    # blockquote => quotation
    elif node.name == 'blockquote':
        accum.append('\\begin{quotation}\n')
        convert_children(node, accum, doEscape)
        accum.append('\\end{quotation}\n')

    # br => line break
    elif node.name == 'br':
        accum.append(r' \\')

    # cite => cite
    elif node.name == 'cite':
        accum.append(r'\cite{')
        convert_children(node, accum, doEscape)
        accum.append('}')

    # code => typewriter text
    elif node.name == 'code':
        accum.append(r'\texttt{')
        convert_children(node, accum, doEscape)
        accum.append(r'}')

    # dd => just a paragraph
    elif node.name == 'dd':
        convert_children(node, accum, doEscape)
        accum.append('\n')

    # div => it depends...
    elif node.name == 'div':
        # Patch the bibliography
        if has_class(node, 'bibliography'):
            bib = node.dl # assume exactly one
            add_class(bib, 'bibliography')
            for entry in bib.find_all('dt'):
                add_class(entry, 'bibliography')
        # Always convert children of div
        convert_children(node, accum, doEscape)

    # dl => description list
    elif node.name == 'dl':
        if has_class(node, 'bibliography'):
            accum.append(r'\begin{thebibliography}{ABCD}')
            convert_children(node, accum, doEscape)
            accum.append(r'\end{thebibliography}')
        else:
            accum.append(r'\begin{description}')
            convert_children(node, accum, doEscape)
            accum.append(r'\end{description}')

    # dt => description item
    elif node.name == 'dt':
        if has_class(node, 'bibliography'):
            temp = ''.join(convert_children(node, [], doEscape))
            accum.append(rf'\bibitem{{{temp}}}')
        elif has_class(node, 'glossary'):
            key = node['id']
            temp = ''.join(convert_children(node, [], doEscape))
            accum.append(rf'\glossitem{{{key}}}{{{temp}}} ')
        else:
            temp = ''.join(convert_children(node, [], doEscape))
            accum.append(rf'\item[{temp}] ')

    # em => italics
    elif node.name == 'em':
        accum.append(r'\emph{')
        convert_children(node, accum, doEscape)
        accum.append(r'}')

    # h1 => chapter title
    elif node.name == 'h1':
        key = node['key']
        accum.append(r'\chapter{')
        convert_children(node, accum, doEscape)
        accum.append(r'}\label{')
        accum.append(key)
        accum.append('}\n')

    # h2 => section title
    elif node.name == 'h2':
        accum.append(r'\section{')
        convert_children(node, accum, doEscape)
        accum.append('}\n')

    # h3 => subsection title
    elif node.name == 'h3':
        accum.append(r'\subsection*{')
        convert_children(node, accum, doEscape)
        accum.append('}\n')

    # list item
    elif node.name == 'li':
        accum.append(r'\item ')
        convert_children(node, accum, doEscape)
        accum.append('\n')

    # ordered list
    elif node.name == 'ol':
        accum.append('\\begin{enumerate}\n')
        convert_children(node, accum, doEscape)
        accum.append('\\end{enumerate}\n')

    # p => paragraph
    elif node.name == 'p':
        accum.append('\n')
        if has_class(node, 'noindent'):
            accum.append(r'\noindent')
            accum.append('\n')
        convert_children(node, accum, doEscape)
        accum.append('\n')

    # pre => preformatted text
    elif node.name == 'pre':
        child = node.contents[0]
        assert child.name == 'code', 'Expected code as child of pre'
        accum.append('\\begin{lstlisting}\n')
        convert_children(child, accum, False)
        accum.append('\\end{lstlisting}\n')

    # strong => bold
    elif node.name == 'strong':
        accum.append(r'\textbf{')
        convert_children(node, accum, doEscape)
        accum.append(r'}')

    # chap => cross-reference of some kind
    elif node.name == 'span':
        # appendix
        if node.has_attr('a'):
            key = node['a']
            accum.append(rf'\appref{{{key}}}')
        # chapter
        elif node.has_attr('c'):
            key = node['c']
            accum.append(rf'\chapref{{{key}}}')
        # glossary
        elif node.has_attr('g'):
            key = node['g']
            accum.append(r'\glossref{')
            convert_children(node, accum, doEscape)
            accum.append('}{')
            accum.append(key)
            accum.append('}')
        # not our problem
        else:
            convert_children(node, accum, doEscape)

    # table
    elif node.name == 'table':
        convert_table(node, accum)

    # unordered list
    elif node.name == 'ul':
        if has_class(node, 'toc'):
            pass
        else:
            accum.append('\\begin{itemize}\n')
            convert_children(node, accum, doEscape)
            accum.append('\\end{itemize}\n')

    # unrecognized
    else:
        print('UNKNOWN', node.name, file=sys.stderr)

    return accum


def convert_children(node, accum, doEscape):
    '''Handle the children of a node.'''
    for child in node:
        convert(child, accum, doEscape)
    return accum


def convert_table(node, accum):
    '''Convert a table.'''
    assert node.name == 'table', 'Node is not a table'
    width = len(node.thead.tr.find_all('th'))
    head = convert_table_row(node.thead.tr, 'th')
    body = [convert_table_row(row, 'td') for row in node.tbody.find_all('tr')]
    rows = [head, *body]
    spec = 'l' * width
    accum.append(f'\\begin{{tabular}}{{{spec}}}\n')
    accum.append('\n'.join(rows))
    accum.append('\n\\end{tabular}\n')


def convert_table_row(row, tag):
    '''Convert a single row of a table.'''
    cells = row.find_all(tag)
    result = []
    for cell in cells:
        temp = convert(cell, [], True)
        result.append(''.join(temp))
    return ' & '.join(result) + r' \\'


def has_class(node, cls):
    '''Check if node has specified class.'''
    return node.has_attr('class') and (cls in node['class'])


def add_class(node, cls):
    '''Add a class to a node.'''
    node['class'] = node.get('class', []) + [cls]


def display(options, text):
    '''Display translated files with header and footer.'''
    head = open(options.head, 'r').read()
    foot = open(options.foot, 'r').read()
    text = text\
        .replace('“', "``")\
        .replace('”', "''")\
        .replace('’', "'")
    print(head)
    print(text)
    print(foot)


def escape(text, doEscape):
    '''Escape special characters if asked to.'''
    if not doEscape:
        return text
    return text\
        .replace('%', r'\%')\
        .replace('_', r'\_')\
        .replace('#', r'\#')\
        .replace('$', r'\$')\
        .replace('&', r'\&')


if __name__ == '__main__':
    options = utils.get_options(
        ['--config', False, 'Path to YAML configuration file'],
        ['--foot', False, 'Path to LaTeX footer file'],
        ['--head', False, 'Path to LaTeX header file'],
        ['--site', False, 'Path to root directory of HTML site']
    )
    html2tex(options)

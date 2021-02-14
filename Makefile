JEKYLL=bundle exec jekyll
BIB=_includes/bib.html
SITE=./_site

CONFIG=_config.yml
INCLUDES=$(wildcard _includes/*)
LAYOUTS=$(wildcard _layouts/*.html)
PAGES=\
	$(wildcard *.md)\
	$(wildcard */index.md)
STYLES=$(wildcard _sass/*/*.scss) $(wildcard css/*.css) $(wildcard css/*.scss)

.DEFAULT: commands

## commands: show available commands
commands:
	@grep -h -E '^##' ${MAKEFILE_LIST} | sed -e 's/## //g' | column -t -s ':'

## build: rebuild site without running server
build:
	${JEKYLL} build

## serve: build site and run server
serve:
	${JEKYLL} serve

## ----

## check: run all checks
check:
	@make bibliography
	@make glossary

## bibliography: compare citations and definitions
bibliography:
	@bin/bibliography.py --bibliography bibliography.md --sources ${PAGES}

## glossary: compare references and definitions
glossary:
	@bin/glossary.py --glossary _data/glossary.yml --sources ${PAGES}

## ----

## clean: clean up stray files
clean:
	@find . -name '*~' -exec rm {} \;

## sterile: clean up and erase generated site
sterile:
	@make clean
	@rm -rf ${SITE}

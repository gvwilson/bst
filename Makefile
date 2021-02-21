JEKYLL=bundle exec jekyll
BIB=_includes/bib.html
SITE=./_site

CONFIG=_config.yml
INCLUDES=$(wildcard _includes/*)
LAYOUTS=$(wildcard _layouts/*.html)
MARKDOWN=$(wildcard *.md) $(wildcard */index.md)
STATIC=$(wildcard _sass/*/*.scss) $(wildcard css/*.css) $(wildcard css/*.scss) $(wildcard js/*.js)

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

${SITE}/index.html: _config.yml ${MARKDOWN} ${INCLUDES} ${LAYOUTS} ${STATIC}
	${JEKYLL} build

## book.tex: create LaTeX file.
book.tex: ${SITE}/index.html bin/html2tex.py
	bin/html2tex.py --config _config.yml --site _site --head tex/head.tex --foot tex/foot.tex > book.tex

## book.pdf: create PDF file.
book.pdf: book.tex
	@pdflatex book
	@pdflatex book

## ----

## check: run all checks
check:
	@make check-bib
	@make check-gloss
	@make check-ref

## check-bib: compare citations and definitions
check-bib:
	@bin/check-bib.py --bibliography bibliography/index.md --sources ${MARKDOWN}

## check-gloss: compare references and definitions
check-gloss:
	@bin/check-gloss.py --glossary _data/glossary.yml --sources ${MARKDOWN}

## check-ref: compare chapter cross-references to chapters and appendices
check-ref:
	@bin/check-ref.py --config _config.yml --sources ${MARKDOWN}

## ----

## clean: clean up stray files
clean:
	@find . -name '*~' -exec rm {} \;
	@rm -f *.aux *.log *.out *.tex *.toc

## sterile: clean up and erase generated site
sterile:
	@make clean
	@rm -rf ${SITE}

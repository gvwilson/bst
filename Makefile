JEKYLL=bundle exec jekyll
BIB=_includes/bib.html
SITE=./_site

CONFIG=_config.yml
INCLUDES=$(wildcard _includes/*)
LAYOUTS=$(wildcard _layouts/*.html)
MARKDOWN=$(wildcard *.md) $(wildcard */index.md)
STATIC=$(wildcard _sass/*/*.scss) $(wildcard css/*.css) $(wildcard css/*.scss) $(wildcard js/*.js)

BIB_IN=_data/bibliography.yml
BIB_OUT=bibliography/index.md
GLOSSARY_IN=_data/glossary.yml
HOME_PAGE=${SITE}/index.html
TERMS_OUT=_data/terms.yml

.DEFAULT: commands

## commands: show available commands
commands:
	@grep -h -E '^##' ${MAKEFILE_LIST} | sed -e 's/## //g' | column -t -s ':'

## build: rebuild site without running server
build: ${BIB_OUT} ${TERMS_OUT}
	${JEKYLL} build

## serve: build site and run server
serve: ${BIB_OUT} ${TERMS_OUT}
	${JEKYLL} serve

## book.tex: create LaTeX file.
book.tex: ${HOME_PAGE} bin/html2tex.py
	bin/html2tex.py --config ${CONFIG} --site _site --head tex/head.tex --foot tex/foot.tex > book.tex

## book.pdf: create PDF file.
book.pdf: book.tex
	@pdflatex book
	@pdflatex book

## make-bib: create Markdown version of bibliography
make-bib: ${BIB_OUT}

## make-terms: create YAML file listing terms per chapter.
make-terms: ${TERMS_OUT}

${BIB_OUT}: ${BIB_IN} bin/make-bib.py
	bin/make-bib.py --input ${BIB_IN} --output ${BIB_OUT}

${TERMS_OUT}: bin/make-terms.py ${MARKDOWN} ${GLOSSARY_IN}
	bin/make-terms.py --config ${CONFIG} --glossary ${GLOSSARY_IN} --output ${TERMS_OUT}

${HOME_PAGE}: ${CONFIG} ${MARKDOWN} ${INCLUDES} ${LAYOUTS} ${STATIC}
	${JEKYLL} build

## ----

## check: run all checks
check:
	@make check-bib
	@make check-gloss
	@make check-ref

## check-bib: compare citations and definitions
check-bib:
	@bin/check-bib.py --bibliography ${BIB_IN} --sources ${MARKDOWN}

## check-gloss: compare references and definitions
check-gloss:
	@bin/check-gloss.py --glossary ${GLOSSARY_IN} --sources ${MARKDOWN}

## check-ref: compare chapter cross-references to chapters and appendices
check-ref:
	@bin/check-ref.py --config ${CONFIG} --sources ${MARKDOWN}

## ----

## clean: clean up stray files
clean:
	@find . -name '*~' -exec rm {} \;
	@rm -f *.aux *.log *.out *.tex *.toc

## sterile: clean up and erase generated site
sterile:
	@make clean
	@rm -rf ${SITE}

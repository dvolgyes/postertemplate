#!/usr/bin/make

GLD={{cookiecutter.gitlatexdiff}}
GLD_OPTIONS={{cookiecutter.gitlatexdiff_options}}
TEXBASE={{cookiecutter.poster_file}}
TEXENGINE={{cookiecutter.tex_engine}}
BIBENGINE={{cookiecutter.bib_engine}}

pdf:
	@mkdir -p build
	${TEXENGINE} -halt-on-error -interaction=batchmode ${TEXBASE}.tex -output-directory=build
	${TEXENGINE} -halt-on-error -interaction=batchmode ${TEXBASE}.tex -output-directory=build
	${TEXENGINE} ${TEXBASE}
	${TEXENGINE} -halt-on-error -interaction=batchmode ${TEXBASE}.tex -output-directory=build
	${TEXENGINE} -halt-on-error -interaction=batchmode ${TEXBASE}.tex -output-directory=build
	${TEXENGINE} -halt-on-error -interaction=batchmode ${TEXBASE}.tex -output-directory=build

diff: pdf
	${GLD} ${GLD_OPTIONS} --main ${TEXBASE}.tex  HEAD~1 --

figures-zip:
	# test figures
	@zip -r -j figures.zip figs -i figs

tables-zip:
	@zip -r -j tables.zip tables -i tables

clean:
	@rm -r build
	@mkdir -p build
	@rm -r figures.zip tables.zip

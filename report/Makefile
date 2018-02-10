FILE=main

UNAME := $(shell uname)

ifeq ($(UNAME), Darwin)
OPENCMD=open
endif
ifeq ($(UNAME), Linux)
OPENCMD=xdg-open
endif

all: 
	pdflatex ${FILE}

clean:
	rm -rf *~ *.aux *.bbl *.dvi *.log *.out *.blg *.toc *.fdb_latexmk *.fls *.tdo *.bcf

view:
	open ${FILE}.pdf

.PHONY: all clean view fast watch

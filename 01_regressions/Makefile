
FLAGS = --from markdown \
	--standalone \
	--bibliography=bibliography.bib \
	--csl=bibliography.csl

METADATA = metadata.yaml

objects = \
	00_theory.md \
	01_linear.md \
	02_multi.md \
	03_logistic.md \
	04_conclusion.md


main: single.html
run: main
	xdg-open single.html

all: single.html single.md single.pdf

pdf: single.pdf

%.md : %.py
	if [ -f $< ]; then python $< > $@; fi

single.md: $(objects)
	pandoc $(FLAGS) --output $@ $(objects) $(METADATA)

single.pdf:  $(METADATA)
	pandoc $(FLAGS) --output $@ $(objects) $(METADATA)

single.html: $(objects) $(METADATA)
	pandoc $(FLAGS) --output $@ $(objects) $(METADATA)

clean:
	rm *.pdf *.html


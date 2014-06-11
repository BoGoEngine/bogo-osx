all: clean build install

clean:
	rm -rf dist

build:
	python setup.py py2app -A

install:
	rm -rf "~/Library/Input Methods/BoGo.app"
	cp -Rf dist/BoGo.app ~/Library/Input\ Methods/


.PHONY: build

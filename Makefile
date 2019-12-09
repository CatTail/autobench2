init:
	pip install -r requirements.txt

test:
	nosetests tests

install:
	pip install --editable .

package: clean
	python setup.py sdist bdist_wheel

upload: test package
	twine upload --repository pypi dist/*

clean:
	rm -rf ./dist ./build ./autobench2.egg-info

.PHONY: init test package clean

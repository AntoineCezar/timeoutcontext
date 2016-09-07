.PHONY: clean-pyc clean-build docs clean
BROWSER="firefox"

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "test-all - run tests on every Python version with tox"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "release - package and upload a release"
	@echo "dist - package"
	@echo "develop - link the package into the active Python's site-packages"
	@echo "install - install the package to the active Python's site-packages"

clean: clean-build clean-pyc clean-test clean-coverage

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/

clean-coverage:
	rm -f .coverage
	rm -fr htmlcov/

lint:
	flake8 timeoutcontext tests

test:
	python setup.py test

doctest:
	python -m doctest timeoutcontext/signal_timeout.py

test-all:
	tox

coverage: clean-coverage .coverage
	coverage report -m

coverage-html: clean-coverage .coverage
	coverage html
	$(BROWSER) htmlcov/index.html

.coverage:
	coverage run --source timeoutcontext setup.py test

docs:
	rm -f docs/timeoutcontext.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ timeoutcontext
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

release: clean
	python setup.py sdist upload
	python setup.py bdist_wheel upload

dist: clean
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

develop: clean
	python setup.py develop

install: clean
	python setup.py install

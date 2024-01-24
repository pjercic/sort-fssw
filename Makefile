init:
	pip install -r requirements.txt

test:
	py.test tests
	nosetests tests

.PHONY: init test


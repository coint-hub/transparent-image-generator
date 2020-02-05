setup: venv
	venv/bin/pip install --upgrade pip==20.0.2
	venv/bin/pip install -e .[dev]

venv:
	python3.7 -m venv venv

dist: setup
	venv/bin/python setup.py sdist bdist_wheel
	venv/bin/twine upload dist/*

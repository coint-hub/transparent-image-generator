setup: venv
	venv/bin/pip install --upgrade pip==8.1.2
	venv/bin/pip install -e . 
venv:
	virtualenv -p python3.5 venv

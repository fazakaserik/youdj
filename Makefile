init:
	pip install -r requirements.txt

test:
	nosetests tests

clean:
    rm -rf __pycache__

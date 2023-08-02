.PHONY: build-env

build-env:
	@python3 -m venv .venv && \
	. .venv/bin/activate && \
	python3 -m pip install --upgrade pip setuptools && \
	pip3 install -r requirements.txt

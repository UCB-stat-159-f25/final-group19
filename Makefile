ENV_NAME = inaugural-address
PYTHON = python

.PHONY: all env data clean

all: env data

env:
	@if conda env list | grep -q "^$(ENV_NAME) "; then \
		conda env update -n $(ENV_NAME) -f environment.yaml; \
	else \
		conda env create -f environment.yaml; \
	fi
	@conda run -n inaugural-address python -m spacy download en_core_web_sm

data:
	$(PYTHON) make_data.py

clean: 
	rm -rf data/*
	rm -rf __pycache__
	rm -rf .pytest_cache

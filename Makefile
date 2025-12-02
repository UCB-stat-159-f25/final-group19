ENV_NAME = inaugural-address
PYTHON = python

.PHONY: all env data

all: env data

env:
	@if conda env list | grep -q "^$(ENV_NAME) "; then \
		conda env update -n $(ENV_NAME) -f environment.yaml; \
	else \
		conda env create -f environment.yaml; \
	fi

data:
	$(PYTHON) make_data.py

clean: 
	rm -rf data/*

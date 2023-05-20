SHELL = /bin/bash

.DEFAULT_GOAL := all

## help: Display list of commands
.PHONY: help
help: Makefile
	@sed -n 's|^##||p' $< | column -t -s ':' | sed -e 's|^| |'

## all: Run all targets
.PHONY: all
all: init style test

## init: Bootstrap app.
.PHONY: init
init:
	pre-commit install -t pre-commit
	poetry install --no-root

## init: Run tests
.PHONY: tests
test:
	poetry run pytest -s tests

## coverage: Execute code coverage
.PHONY: coverage
coverage:
	poetry run pytest --cov=tdd -s tests

## style: Check lint, code styling rules.
.PHONY: style
.PHONY: format
style format:
	pre-commit run -a

## clean: Remove temporary files
.PHONY: clean
clean:
	poetry remove env 3.8


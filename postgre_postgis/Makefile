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
	poetry install --no-root

## init: Run tests
test:
	echo "Nothing Setup"

## style: Check lint, code styling rules.
.PHONY: style
style:
	echo "Nothing Setup"

## format: Check lint, code styling rules.
.PHONY: format
format:
	echo "Nothing Setup"

## clean: Remove temporary files
.PHONY: clean
clean:
	-poetry remove env 3.10


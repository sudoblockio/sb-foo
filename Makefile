.PHONY: test help

test:  # Run all the tests
	pytest tests

install:
	pip install -e sb_foo_client
	pip install -e sb_foo_indexer # .[dev]

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'

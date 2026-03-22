.PHONY: simplest directories multipage

simplest:
	uv run python htmlsite.py --source_dir examples/simplest/src --output_dir examples/simplest/site
	uv run python -m http.server --directory examples/simplest/site

directories:
	uv run python htmlsite.py --input_dir examples/directories/src --output_dir examples/directories/site
	uv run python -m http.server --directory examples/directories/site

multipage:
	uv run python htmlsite.py --input_dir examples/multipage/src --output_dir examples/multipage/site
	uv run python -m http.server --directory examples/multipage/site

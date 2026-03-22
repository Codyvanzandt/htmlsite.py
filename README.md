# htmlsite.py

Static site generators are sleek little tools. But for all their sleekness, sometimes you find yourself wishing for even less.
**htmlsite.py** is less. A *lot* less. It's templates and partials for index.html files -- and not a single feature more. 

If your ideal static site structure looks like this...

<pre>
src/
├── _partials/
│   └── navbar.html
├── _templates/
│   └── base.html
├── index.html
├── about/
│   └── index.html
└── contact/
    └── index.html
</pre>

...then your ideal static site generation looks a lot like **htmlsite.py**.

## Installation

**htmlsite.py** is a single 65-line Python file that depends only upon the [Jinja2 templating engine](https://jinja.palletsprojects.com/en/stable/) and tools within the Python standard library. 

Installation means [pip installing Jinja2](https://pypi.org/project/Jinja2/), dropping the [htmlsite.py file](https://github.com/Codyvanzandt/htmlsite.py/blob/main/htmlsite.py) into your codebase, and running it with Python 3.7+. 

## Usage

**htmlsite.py** assumes your HTML files are written in the Jinja templating language and structured as `index.html` files inside of directories.

Point it at your source directory and tell it where to write the output:

```bash
python htmlsite.py --source_dir <src> --output_dir <site>
```

`source_dir` is the top-level directory containing your index.html files, defaulting to `src`. `output_dir` is where **htmlsite.py** will output your completed static site, defaulting to `site`. 

Prefixing a directory with an underscore (e.g., "_templates") tells **htmlsite.py** not to render it.

## Examples

The examples directory in this repository contains three simple (but progressively less simple) examples: `simplest`, `directories`, and `multipage`.




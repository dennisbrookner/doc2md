# Docstring to Markdown Parser

Intended to provide quick static documentations for packages hosted on GitHub.
This package parses the docstrings of any installed Python module
into a simple Markdown format, grouped by
_submodules_, _classes_ and _functions_.
The resulting hierarchy is following the namespace based on the
package's `__all__` attributes, thus correctly documenting possibly shortened
import paths.


## Example
Assuming the following package structure
```
module
├── submodule
│   ├── __init__.py
│   └── bar.py
├── __init__.py
└── foo.py
```
with the classes `module.foo.Foo` and `module.submodule.bar.Bar`.
In case your module is configured to import all possible components on the top level
(_i.e._ `module.Foo` and `module.Bar`),
_doc2md_ will automatically pick this up and document the classes in the correct
namespace:
```
# **module** Package Overview

## Submodules
* `module.submodule`

## Classes
* `Foo`
* `Bar`
```


## Installation
* `git clone`
* `pip install -e .`


## Usage
:warning: Work in progress, currently only the overview can be printed :warning:

Use `doc2md MODULENAME` from the command line (`doc2md --help` for help).

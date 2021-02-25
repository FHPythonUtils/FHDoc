[![GitHub top language](https://img.shields.io/github/languages/top/FHPythonUtils/FHDoc.svg?style=for-the-badge)](../../)
[![Repository size](https://img.shields.io/github/repo-size/FHPythonUtils/FHDoc.svg?style=for-the-badge)](../../)
[![Issues](https://img.shields.io/github/issues/FHPythonUtils/FHDoc.svg?style=for-the-badge)](../../issues)
[![License](https://img.shields.io/github/license/FHPythonUtils/FHDoc.svg?style=for-the-badge)](/LICENSE.md)
[![Commit activity](https://img.shields.io/github/commit-activity/m/FHPythonUtils/FHDoc.svg?style=for-the-badge)](../../commits/master)
[![Last commit](https://img.shields.io/github/last-commit/FHPythonUtils/FHDoc.svg?style=for-the-badge)](../../commits/master)
[![PyPI Downloads](https://img.shields.io/pypi/dm/fhdoc.svg?style=for-the-badge)](https://pypistats.org/packages/fhdoc)
[![PyPI Total Downloads](https://img.shields.io/badge/dynamic/json?style=for-the-badge&label=total%20downloads&query=%24.total_downloads&url=https%3A%2F%2Fapi.pepy.tech%2Fapi%2Fprojects%2Ffhdoc)](https://pepy.tech/project/fhdoc)
[![PyPI Version](https://img.shields.io/pypi/v/fhdoc.svg?style=for-the-badge)](https://pypi.org/project/fhdoc)

<!-- omit in TOC -->
# FHDoc - Python documentation generator

<img src="readme-assets/icons/name.png" alt="Project Icon" width="750">


Python docstring-based documentation generator for lazy perfectionists.

Forked from vemel/handsdown

- [Features](#features)
- [Do you need fhdoc?](#do-you-need-fhdoc)
- [Examples](#examples)
- [Using](#using)
	- [From command line](#from-command-line)
	- [As a GitHub Pages manager](#as-a-github-pages-manager)
	- [Deploy on Read the Docs](#deploy-on-read-the-docs)
	- [Build static HTML](#build-static-html)
	- [As a module](#as-a-module)
- [Installation](#installation)
- [Documentation](#documentation)
- [Install With PIP](#install-with-pip)
- [Language information](#language-information)
	- [Built for](#built-for)
- [Install Python on Windows](#install-python-on-windows)
	- [Chocolatey](#chocolatey)
	- [Download](#download)
- [Install Python on Linux](#install-python-on-linux)
	- [Apt](#apt)
- [How to run](#how-to-run)
	- [With VSCode](#with-vscode)
	- [From the Terminal](#from-the-terminal)
- [Download Project](#download-project)
	- [Clone](#clone)
		- [Using The Command Line](#using-the-command-line)
		- [Using GitHub Desktop](#using-github-desktop)
	- [Download Zip File](#download-zip-file)
- [Community Files](#community-files)
	- [Licence](#licence)
	- [Changelog](#changelog)
	- [Code of Conduct](#code-of-conduct)
	- [Contributing](#contributing)
	- [Security](#security)
	- [Support](#support)
	- [Rationale](#rationale)

## Features

- [PEP 257](https://www.python.org/dev/peps/pep-0257/),
  [Google](http://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings),
  [Sphinx](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html)
  and [reStructuredText](https://www.python.org/dev/peps/pep-0287/)
  docstrings support. All of them are converted to a valid Markdown.
- Works with [Django](https://www.djangoproject.com/) and [Flask](https://palletsprojects.com/p/flask/) apps
- Can be used locally, or
  [right on GitHub](https://github.com/FHPythonUtils/fhdoc/blob/master/DOCS/README.md) or even deployed on
- Signatures for every class, function, property and method.
- Support for type annotations. Even for the ones from the `__future__`!
- Nice list of all modules in [Modules](https://github.com/FHPythonUtils/fhdoc/blob/master/DOCS/MODULES.md)
- Gather all scattered `README.md` in submodules to one place
- Find related source code from every doc section.
- Make links by just adding `module.import.String` to docs.
- Do you use type annotations? Well, you get auto-discovery of related modules for free!

## Do you need fhdoc?

You definitely *do* if you:

- prefer to automate documentation builds
- work with a team and plan to simplify knowledge sharing
- want to show your project without navigating through a source code
- build `Django` or `Flask` applications, and even if you do not
- are proud of your project and not afraid to show it
- love Open Source

And probably *do not* if you:

- not very into docstrings and type annotations
- like to abstract a documentation away from the way things really are
- use [Pandas docstrings](https://pandas.pydata.org/pandas-DOCS/stable/development/contributing_docstring.html)
  as they are not supported yet

## Examples

- [Main](https://github.com/FHPythonUtils/fhdoc/blob/master/examples/main_example.py) with [generated output](https://github.com/FHPythonUtils/fhdoc/tree/master/DOCS/examples/main_example.md)
- [RST docstrings](https://github.com/FHPythonUtils/fhdoc/blob/master/examples/rst_docstrings.py) with [generated output](https://github.com/FHPythonUtils/fhdoc/tree/master/DOCS/examples/rst_docstrings.md)
- [Google docstrings](https://github.com/FHPythonUtils/fhdoc/blob/master/examples/google_docstrings.py) with [generated output](https://github.com/FHPythonUtils/fhdoc/tree/master/DOCS/examples/google_docstrings.md)
- [PEP 257 docstrings](https://github.com/FHPythonUtils/fhdoc/blob/master/examples/pep257_docstrings.py) with [generated output](https://github.com/FHPythonUtils/fhdoc/tree/master/DOCS/examples/pep257_docstrings.md)
- [Sphinx docstrings](https://github.com/FHPythonUtils/fhdoc/blob/master/examples/sphinx_docstrings.py) with [generated output](https://github.com/FHPythonUtils/fhdoc/tree/master/DOCS/examples/sphinx_docstrings.md)
- [Type annotations](https://github.com/FHPythonUtils/fhdoc/blob/master/examples/typed.py) with [generated output](https://github.com/FHPythonUtils/fhdoc/tree/master/DOCS/examples/typed.md)
- [Comment-style type annotations](https://github.com/FHPythonUtils/fhdoc/blob/master/examples/comment_typed.py) with [generated output](https://github.com/FHPythonUtils/fhdoc/tree/master/DOCS/examples/comment_typed.md)

## Using

### From command line

Just go to your favorite project that has lots of docstrings but missing
auto-generated docs and let `fhdoc` do the thing.

```bash
cd ~/my/project

# build documentation *.md* files in DOCS/* directory
fhdoc

# or provide custom output directory: output_dir/*
fhdoc -o output_dir

# generate docs only for my_module, but exclude migrations
fhdoc my_module --exclude my_module/migrations

# generate documentation for deployment
fhdoc --external `git config --get remote.origin.url` -n ProjectName
```

Navigate to `DOCS/README.md` to check your new documentation!

### As a GitHub Pages manager

With `--external` CLI flag, `fhdoc` generates all required configuration
for [GitHub Pages](https://pages.github.com/), so you just need to setup your
GitHub repository.

```bash
# Generate documentation that points to master branch
# do not use custom output location, as `GitHub Pages`
# works only with `docs` directory
fhdoc --external `git config --get remote.origin.url`

# or specify GitHub url directly
fhdoc --external https://github.com/<user>/<project>/blob/master/
```

- Generate documentation with `--external` flag as shown above, do not use `--output`
  flag, only `docs` folder is supported by `GitHub Pages`
- Commit and push all changes a to `master` branch.
- Set your GitHub project `Settings` > `GitHub Pages` > `Source` to `master branch /docs folder`

All set! You can change `DOCS/_config.yml` to add your own touch.

With `--external` flag links to your source are absolute and point to your GitHub repo. If you
still want to have relative links to source, e.g. for using docs locally,
generate docs to another folder

```bash
# `docs_local` folder will be created in your project root
# you probably want to add it to .gitignore
fhdoc -o docs_local
```

### Deploy on Read the Docs

With `--external` CLI flag, `fhdoc` generates all required configuration
for [Read the Docs](https://readthedocs.org/), so you just need to to add your
GitHub repository to `Read the Docs`.

```bash
# Generate documentation that points to master branch
# do not use custom output location, as `GitHub Pages`
# works only with `docs` directory
fhdoc --external `git config --get remote.origin.url`

# or specify GitHub url directly
fhdoc --external https://github.com/<user>/<project>/blob/master/
```

- Generate documentation with `--external` flag as shown above, do not use `--output`
  flag, only `docs` folder is supported by `Read the Docs`
- Commit and push all changes a to `master` branch.
- Add your repository on [Read the Docs](https://readthedocs.org/)

All set! You can change `.readthedocs.yml` and `mkdocs.yml` to add your own touch.

### Build static HTML

```bash
# Generate documentation that points to master branch
# with source links pointing to your repository
# this command also creates `mkdocs.yml`
fhdoc --external `git config --get remote.origin.url`

# Run mkdocs to build HTML
mkdocs build
```

### As a module

```python
from fhdoc.generator import Generator
from fhdoc.utils.path_finder import PathFinder

# this is our project root directory
repo_path = Path.cwd()

# this little tool works like `pathlib.Path.glob` with some extra magic
# but in this case `repo_path.glob("**/*.py")` would do as well
path_finder = PathFinder(repo_path, "**/*.py")

# no docs for tests and build
path_finder.exclude("tests/*", "build/*")

# initialize generator
fhdoc = Generator(
	input_path=repo_path,
	output_path=repo_path / 'output',
	source_paths=path_finder.glob("**/*.py")
)

# generate all docs at once
fhdoc.generate_docs()

# or generate just for one doc
fhdoc.generate_doc(repo_path / 'my_module' / 'source.py')

# and generate index.md file
fhdoc.generate_index()

# navigate to `output` dir and check results
```

## Installation

Install using `pip` from PyPI

```bash
pip install fhdoc
```

## Documentation
See the [Docs](/DOCS/README.md) for more information.

## Install With PIP
```python
pip install fhdoc
```

Head to https://pypi.org/project/fhdoc/ for more info

## Language information
### Built for
This program has been written for Python 3 and has been tested with
Python version 3.9.0 <https://www.python.org/downloads/release/python-380/>.

## Install Python on Windows
### Chocolatey
```powershell
choco install python
```
### Download
To install Python, go to <https://www.python.org/> and download the latest
version.

## Install Python on Linux
### Apt
```bash
sudo apt install python3.9
```

## How to run
### With VSCode
1. Open the .py file in vscode
2. Ensure a python 3.9 interpreter is selected (Ctrl+Shift+P > Python:Select
Interpreter > Python 3.9)
3. Run by pressing Ctrl+F5 (if you are prompted to install any modules, accept)
### From the Terminal
```bash
./[file].py
```

## Download Project
### Clone
#### Using The Command Line
1. Press the Clone or download button in the top right
2. Copy the URL (link)
3. Open the command line and change directory to where you wish to
clone to
4. Type 'git clone' followed by URL in step 2
```bash
$ git clone https://github.com/FHPythonUtils/FHDoc
```

More information can be found at
<https://help.github.com/en/articles/cloning-a-repository>

#### Using GitHub Desktop
1. Press the Clone or download button in the top right
2. Click open in desktop
3. Choose the path for where you want and click Clone

More information can be found at
<https://help.github.com/en/desktop/contributing-to-projects/cloning-a-repository-from-github-to-github-desktop>

### Download Zip File

1. Download this GitHub repository
2. Extract the zip archive
3. Copy/ move to the desired location

## Community Files
### Licence
MIT License
Copyright (c) FredHappyface
(See the [LICENSE](/LICENSE.md) for more information.)

### Changelog
See the [Changelog](/CHANGELOG.md) for more information.

### Code of Conduct
Online communities include people from many backgrounds. The *Project*
contributors are committed to providing a friendly, safe and welcoming
environment for all. Please see the
[Code of Conduct](https://github.com/FHPythonUtils/.github/blob/master/CODE_OF_CONDUCT.md)
 for more information.

### Contributing
Contributions are welcome, please see the
[Contributing Guidelines](https://github.com/FHPythonUtils/.github/blob/master/CONTRIBUTING.md)
for more information.

### Security
Thank you for improving the security of the project, please see the
[Security Policy](https://github.com/FHPythonUtils/.github/blob/master/SECURITY.md)
for more information.

### Support
Thank you for using this project, I hope it is of use to you. Please be aware that
those involved with the project often do so for fun along with other commitments
(such as work, family, etc). Please see the
[Support Policy](https://github.com/FHPythonUtils/.github/blob/master/SUPPORT.md)
for more information.

### Rationale
The rationale acts as a guide to various processes regarding projects such as
the versioning scheme and the programming styles used. Please see the
[Rationale](https://github.com/FHPythonUtils/.github/blob/master/RATIONALE.md)
for more information.

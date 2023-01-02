# tabla-tools

[![PyPI](https://img.shields.io/pypi/v/tabla-tools.svg)](https://pypi.org/project/tabla-tools/)
[![Changelog](https://img.shields.io/github/v/release/lukegrecki/tabla-tools?include_prereleases&label=changelog)](https://github.com/lukegrecki/tabla-tools/releases)
[![Tests](https://github.com/lukegrecki/tabla-tools/workflows/Test/badge.svg)](https://github.com/lukegrecki/tabla-tools/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/lukegrecki/tabla-tools/blob/master/LICENSE)

A CLI tool for written tabla notation

## Installation

Install this tool using `pip`:

    pip install tabla-tools

## Usage

For help, run:

    tabla-tools --help

You can also use:

    python -m tabla_tools --help

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd tabla-tools
    python -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest

from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="tabla-tools",
    description="A CLI tool for written tabla notation",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Luke Grecki",
    url="https://github.com/lukegrecki/tabla-tools",
    project_urls={
        "Issues": "https://github.com/lukegrecki/tabla-tools/issues",
        "CI": "https://github.com/lukegrecki/tabla-tools/actions",
        "Changelog": "https://github.com/lukegrecki/tabla-tools/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["tabla_tools"],
    entry_points="""
        [console_scripts]
        tabla-tools=tabla_tools.cli:cli
    """,
    install_requires=["click"],
    extras_require={"test": ["pytest", "black"]},
    python_requires=">=3.7",
)

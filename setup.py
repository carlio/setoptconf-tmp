import os.path
import re

from setuptools import setup, find_packages


def get_version():
    init = os.path.join(os.path.dirname(__file__), "setoptconf/__init__.py")
    source = open(init, "r").read()
    version = re.search(r"__version__ = '(?P<version>[^']+)'", source).group("version")
    return version


def get_description():
    readme = os.path.join(os.path.dirname(__file__), "README.rst")
    return open(readme, "r").read()


setup(
    name="setoptconf",
    version=get_version(),
    author="Jason Simeone",
    author_email="jay@classless.net",
    license="MIT",
    keywords=["settings", "options", "configuration", "config", "arguments"],
    description="A module for retrieving program settings from various" " sources in a consistant method.",
    long_description=get_description(),
    url="https://github.com/jayclassless/setoptconf",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=find_packages(exclude=["test.*", "test"]),
    extras_require={"YAML": ["pyyaml"]},
)

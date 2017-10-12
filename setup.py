import ast
import re
from io import open
from setuptools import setup, find_packages
from pip.req import parse_requirements

# get __version__ in __init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')
with open('jsoncrawl/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

# load README.rst
with open('README.rst', 'r', encoding='utf-8') as f:
    readme = f.read()

# load requirements-dev.txt
requirements_dev = parse_requirements('requirements-dev.txt', session=False)
reqs_dev = [str(i.req) for i in requirements_dev]

setup(
    name="jsoncrawl",
    version=version,
    url="https://github.com/json-transformations/jsoncrawl",
    keywords=["json", "tree", "node", "walk", "crawl", "visitor"],

    author="Brian Peterson",
    author_email="bpeterso2000@yahoo.com",

    description="Traverse JSON trees; visit each node; yield results.",
    long_description=readme,

    packages=find_packages(include=['jsoncrawl']),
    include_package_data=True,
    zipsafe=False,

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ],
    test_suite='tests',
    test_requires=reqs_dev,
    setup_requires=['pytest-runner']
)


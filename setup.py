# -*- coding: utf-8 -*-

from setuptools import setup
from codecs import open
from os import path
import re

package_name = "radonpy"

root_dir = path.abspath(path.dirname(__file__))

def _requirements():
    return [name.rstrip() for name in open(path.join(root_dir, 'requirements.txt')).readlines()]


with open(path.join(root_dir, package_name, '__init__.py')) as f:
    init_text = f.read()
    version = re.search(r'__version__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    license = re.search(r'__license__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    author = re.search(r'__author__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    author_email = re.search(r'__author_email__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    url = re.search(r'__url__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)

assert version
assert license
assert author
assert author_email
assert url


setup(
    name=package_name,
    packages=[
        package_name, package_name+'/core', package_name+'/ff', package_name+'/ff/ff_dat',
        package_name+'/sim', package_name+'/sim/preset'
    ],
    package_data={'': [package_name+'/ff/ff_dat/*.json']},
    include_package_data=True,
    install_requires=[
        'numpy',
        'pandas',
        'scipy',
        'psutil',
        'matplotlib',
        'rdkit>=2020.03',
        'mdtraj>=1.9',
        'minepy',
    ],
    extras_require={
        'sim':[
            'lammps>=2020.03.03'
        ],
    },

    platforms=['Linux', 'Mac OS-X', 'Unix', 'Windows'],
    python_requires=">=3.7",
    tests_require=[],

    version=version,
    license=license,
    author=author,
    author_email=author_email,
    url=url,
    description='RadonPy is a Python library to automate physical property calculations for polymer informatics.',
    keywords='polymer informatics, molecular dynamics',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)


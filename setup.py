from setuptools import setup, find_packages
from os import sep
from os.path import join as opj
from doc2md import __version__

NAME = 'doc2md'
DESCR = 'Simple Python docstring to Markdown parser.'
packages = [NAME]+[f'{NAME}.'+i for i in find_packages(NAME)]

setup(
    name             = NAME,
    version          = __version__,
    author           = 'Leo Komissarov',
    author_email     = 'leonid.komissarov@gmail.com',
    url              = f'https://github.com/oiao/{NAME}',
    download_url     = f'https://github.com/oiao/{NAME}/archive/master.zip',
    license          = 'GPLv3+',
    description      = DESCR,
    classifiers      = [
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Documentation',
            'Topic :: Documentation',
            'Programming Language :: Python :: 3.6',
    ],
    keywords         = ['documentation, docstrings, markdown'],
    python_requires  = '>=3.6',
    install_requires = [],
    packages         = packages,
    package_dir      = {NAME : NAME},
    package_data     = {NAME : ['tests/*']},
    scripts          = [opj('scripts', 'doc2md')],
)

import inspect as I
from typing import *
import sys
from os.path import join as opj

__version__ = '0.1'
__all__ = [
    'sort_modules',
    'print_overview',
    '__version__'
    ]


def sort_modules(module):
    ret = {
        'name'      : module.__name__ if hasattr(module, '__name__') else None,
        'modules'   : [],
        'classes'   : [],
        'functions' : [],
        'others'    : [],
        }
    ga = lambda string: getattr(module, string)

    for m in module.__all__:
        if I.ismodule( ga(m) ):
            ret['modules'].append( sort_modules(ga(m)) )
        elif I.isclass( ga(m) ):
            ret['classes'].append(m)
        elif I.isfunction( ga(m) ):
            ret['functions'].append(m)
        else:
            ret['others'].append(m)

    return ret


def print_to(string, fname=None):
    ''' Print either to stdout or fname '''
    if fname is not None:
        with open(fname, 'w') as f:
            print(string, file=f)
    else:
        print(string)


def print_overview(sorted_modules, level=1, dirname=None) -> str:
    d = sorted_modules

    strname = f"**{d['name']}**"
    ret = f"{level*'#'} **{d['name']}** Package Overview\n\n"

    v = d['modules']
    if v != []:
        ret += f"{(level+1)*'#'} Submodules\n"
        for i in v:
            ret += f"* `{i['name']}`\n"
        ret += '\n'


    for k in ['classes', 'functions', 'others']:
        v = d[k]
        if v != []:
            ret += f"{(level+1)*'#'} {k.capitalize()}\n"
            for i in v:
                ret += f"* `{i}`\n"
        ret += '\n'

    print_to(ret, opj(dirname, f"{d['name']}.doverview.md")) if dirname else print_to(ret)

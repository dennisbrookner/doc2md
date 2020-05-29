import inspect as I
from typing import *
import sys
from os.path import join as opj

__version__ = '0.1'
__all__ = [
    'sort_modules',
    'print_overview',
]


def sort_modules(module) -> Dict:
    """ Run inspect on `module`, filter by component types """
    ret = {
        'name'      : module.__name__ if hasattr(module, '__name__') else None,
        'modules'   : [],
        'classes'   : [],
        'functions' : [],
        'others'    : [],
        }
    ga = lambda string: getattr(module, string)

    if not hasattr(module, '__all__'):
        return ret

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


def print_overview(sorted_modules, level=1, dirname=None, full=False) -> str:
    d = sorted_modules

    ret = f"{level*'#'} **{d['name']}** Module Overview\n\n"

    v = d['modules']
    if v != []:
        ret += f"{(level+1)*'#'} Submodules\n"
        for i in v:
            ret += f"* `{i['name']}`\n"
        ret += '\n'

    if not full:
        for k in ['classes', 'functions', 'others']:
            v = d[k]
            if v != []:
                ret += f"{(level+1)*'#'} {k.capitalize()}\n"
                for i in v:
                    ret += f"* `{i}`\n"
            ret += '\n'

    else:
        for k in ['classes', 'functions', 'others']:
            v = d[k]
            if v != []:
                ret += f"{(level+1)*'#'} {k.capitalize()}\n"
                for i in v:
                    ret += f"* `{i}`\n"
            ret += '\n'


    print_to(ret, opj(dirname, f"{d['name']}.md")) if dirname else print_to(ret)

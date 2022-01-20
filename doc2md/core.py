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
        'doc'       : module.__doc__,
        'modules'   : [],
        'classes'   : [],
        'functions' : [],
        'others'    : [],
        }

    if not hasattr(module, '__all__'):
        return ret

    for m in module.__all__:
        a = getattr(module, m)
        if I.ismodule(a):
            ret['modules'].append(sort_modules(a))
        elif I.isclass(a):
            ret['classes'].append((m,a))
        elif I.isfunction(a):
            ret['functions'].append((m,a))
        else:
            ret['others'].append((m,None))

    return ret


def print_to(string, fname=None):
    ''' Print either to stdout or fname '''
    if fname is not None:
        with open(fname, 'w') as f:
            print(string, file=f)
    else:
        print(string)


def print_overview(sorted_modules, level=1, dirname=None, full=True) -> str:
    d = sorted_modules

    ret = f"{level*'#'} **{d['name']}** Module Overview\n"
    if full and d['doc']:
        ret += d['doc']
    ret += '\n'

    v = d['modules']
    if v != []:
        ret += f"{(level+1)*'#'} Submodules\n"
        for i in v:
            ret += f"{(level+2)*'#'} `{i['name']}`\n"
        ret += '\n'

    if not full: # Just print the names
        for k in ['classes', 'functions', 'others']:
            v = d[k]
            if v != []:
                ret += f"{(level+1)*'#'} {k.capitalize()}\n"
                for i in v:
                    ret += f"{(level+2)*'#'} `{i[0]}`\n"
            ret += '\n'

    else: # Print names docstring for functions and class methods
        for k in ['classes', 'functions', 'others']:
            v = d[k]
            if v != []:
                ret += f"{(level+1)*'#'} {k.capitalize()}\n"
                for i in v:
                    ret += f"{(level+2)*'#'} `{i[0]}`\n"
                    if k == 'functions':
                        if i[1].__doc__ is not None:
                            ret += f"\n    ```\n    {i[1].__doc__}\n    ```\n\n"

                    elif k == 'classes':
                        if i[1].__doc__ is not None:
                            ret += f"\n    \n    {i[1].__doc__}\n    \n"

                        methods = {k:v for k,v in i[1].__dict__.items() if not k.startswith('_')}
                        for k,v in methods.items():
                            ret += f"  {(level+2)*'#'} `{i[0]}.{k}`\n"
                            if hasattr(v, '__doc__') and v.__doc__ is not None:
                                ret += f"\n      ```\n      {v.__doc__}\n      ```\n\n"
                ret +='\n'
            ret += '\n'


    print_to(ret, opj(dirname, f"{d['name']}.md")) if dirname else print_to(ret)

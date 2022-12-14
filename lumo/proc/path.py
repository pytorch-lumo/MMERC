import json
import os
import sys
from .config import HOME, EXPROOT, CACHEROOT


def home():
    if HOME:
        return HOME
    return os.path.expanduser("~")


def cache_dir():
    if CACHEROOT:
        return CACHEROOT

    try:
        res = os.path.join(home(), '.cache/lumo')
        os.makedirs(res, exist_ok=True)
    except PermissionError:
        res = os.path.join(home(), '.lumo/.cache')
        os.makedirs(res, exist_ok=True)
    return res


def dataset_cache_dir(name=None):
    if name is None:
        res = os.path.join(cache_dir(), 'datasets', '__default__')
    else:
        res = os.path.join(cache_dir(), 'datasets', name)
    os.makedirs(res, exist_ok=True)
    return res


def libhome():
    return os.path.join(home(), '.lumo')


def exproot():
    if EXPROOT:
        return EXPROOT
    return libhome()


def local_dir():
    from lumo.utils.repository import git_dir
    res = git_dir()
    if res is None:
        res = os.path.dirname(os.path.join(os.getcwd(), sys.argv[0]))
    return res

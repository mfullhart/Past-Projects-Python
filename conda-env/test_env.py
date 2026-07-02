#!/usr/bin/env python3

import importlib

for module_name in ('numpy', 'scipy', 'matplotlib', 'sklearn', 'pandas'):
    try:
        print('importing {}...'.format(module_name), end='')
        module = importlib.import_module(module_name)
        print(' [OK] {} version {}'.format(module_name, module.__version__))
    except ImportError as e:
        print(' [ERROR]', e)

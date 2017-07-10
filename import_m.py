#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys;
if not "/home/a/" in sys.path:
    sys.path.append("/home/zack/work/gitwork/python/sys-module")
if not 'sys_module' in sys.modules:
    b = __import__('sys_module')
else:
    eval('import sys_module')
    b = eval('reload(sys_module)')

b.test()
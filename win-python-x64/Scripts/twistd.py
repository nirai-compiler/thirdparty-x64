#!A:\home\rdb\panda3d\thirdparty\win-python-x64\python.exe
# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.
import os, sys

try:
    import _preamble
except ImportError:
    sys.exc_clear()

sys.path.insert(0, os.path.abspath(os.getcwd()))

from twisted.scripts.twistd import run
run()

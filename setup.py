# -*- coding: utf-8 -*-

# A simple setup script to create an executable running wxPython. This also
# demonstrates the method for creating a Windows executable that does not have
# an associated console.
#
# wxapp.py is a very simple 'Hello, world' type wxPython application
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application

import sys
from cx_Freeze import setup, Executable
import os

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

build_exe_options = {
    "packages": ["os", "wx._xml"],
    "excludes": ["Tkinter"],
    "compressed": True,
    "optimize": 2,
    "path": sys.path + ["sources"]
}

executables = [
    Executable('sources\\phash.py', base=base)
]

setup(name='phash',
      version='0.1',
      description='Parallel hash tool',
      options={"build_exe": build_exe_options},
      executables=executables
      )

UPX = False
if UPX:
    for root, dirs, files in os.walk('build'):
        for dirname in dirs:
            dirpath = os.path.join(root, dirname)
            os.system('upx --best %s\\*.exe %s\\*.dll %s\\*.pyd' % (dirpath, dirpath, dirpath))

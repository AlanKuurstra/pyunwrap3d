import setuptools
from distutils.core import setup, Extension

import numpy
import os

extensions = []

includeDirs = numpy.get_include()
libDirs = "" #giving a blank lib list causes errors!
libs = ""

extensions.append(
    Extension('Unwrap3d',
              sources=['unwrap3dInterface.cpp'],
              include_dirs=[includeDirs],
              install_requires=['numpy'],
              #library_dirs=[libDirs], giving a blank lib list causes errors!
              #libraries=libs, giving a blank lib list causes errors!
              #extra_compile_args=[]
              )
    )

setup(
    name="Unwrap3d",
    version="0.1",
    description = "Python interface to unwrap3d",
    #packages=['PfileInterface'],
    ext_modules=extensions)

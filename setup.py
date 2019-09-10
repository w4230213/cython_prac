from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize(['version2.pyx','version3.pyx', 'version4.pyx']))
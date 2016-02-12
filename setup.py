from setuptools import setup, Extension
from Cython.Build import cythonize

ext_modules = [
    Extension("demo.primes", ["demo/primes.pyx"])
]

setup(
    name = "demo",
    version = 1.0,
    ext_modules = ext_modules,
    packages = ["demo"],
)

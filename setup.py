import numpy
from Cython.Build import cythonize
from setuptools import setup, find_packages, Extension

setup(
    name="styles_and_tricks",
    packages=find_packages(),
    install_requires=[],
    ext_modules=cythonize(
        Extension(
            "tricks.c.cython_utils",
            sources=["tricks/c/cython_utils.pyx"],
            language="c",
            include_dirs=[numpy.get_include(), "tricks/c"],
            library_dirs=[],
            libraries=[],
            extra_compile_args=[],
            extra_link_args=[],
        )
    ),
    package_data={"tricks.c": ["cython_utils.pyx"]},
)

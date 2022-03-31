from importlib.metadata import entry_points
from setuptools import setup

setup(
    name='diff-sqlite',
    version="0.1.0",
    description="Command Line Utility to diff sqlite binary files",
    author='Tom Coppola',
    author_email="tcoppola@naii.com",
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': ['diff-sqlite=main:main'],
    }
)

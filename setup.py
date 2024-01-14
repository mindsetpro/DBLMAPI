# setup.py

from setuptools import setup, find_packages

setup(
    name='dblmapi',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        # Add any dependencies here
    ],
    entry_points={
        'console_scripts': [
            'dblmapi=dblmapi.cli:main',
        ],
    },
)

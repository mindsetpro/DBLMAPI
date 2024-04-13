# setup.py
# made by mindsetpro

from setuptools import setup, find_packages

def main():
    setup(
        name='dblmapi',
        version='1.0.9',
        packages=find_packages(),
        install_requires=[
            # requests coming soon.
        ],
        entry_points={
            'dblmapi_commands': [
                'dblmapi = src.dblmapi_cli:main'
            ]
        }
    )

if __name__ == "__main__":
    main()

from setuptools import setup

# Read the contents of your README file
with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name="pxe",
    version="0.1.0",
    py_modules=["pxe"],
    entry_points={
        'console_scripts': [
            'pxe=pxe:main',
        ],
    },
    author="Denis Laprise",
    author_email="git@2ni.net",
    description="A simple command line utility to execute commands in parallel.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="BSD",
    keywords="parallel execution command line"
)

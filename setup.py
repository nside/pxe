from setuptools import setup

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
    license="BSD",
    keywords="parallel execution command line"
)


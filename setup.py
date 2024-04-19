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
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple command line utility to execute commands in parallel.",
    long_description=long_description,
    long_description_content_type='text/markdown',  # This is important for rendering Markdown on PyPI
    license="BSD",
    keywords="parallel execution command line",
    url="http://example.com/pxe",  # Project home page
)

# PXE

PXE is a command-line utility that allows you to execute multiple shell commands in parallel. It leverages the available CPU cores to optimize execution time and is highly configurable through environment variables.

## Features

- Executes commands in parallel, utilizing the number of CPU cores by default.
- Simple and easy-to-use, adhering to the UNIX philosophy.
- Configurable number of parallel executors via an environment variable.

## Installation

To install PXE, you can use pip after cloning the repository:

```bash
git clone https://example.com/pxe.git
cd pxe
python setup.py install
```

Alternatively, you can install directly using:

```
pip install pxe
```

## Usage

To use PXE, you can pipe a list of commands to it like this:

```
echo -e "ls\npwd" | pxe
```

Or, you can prepare a commands file and execute:

```
cat commands.txt | pxe
```

Environment variable NUM_EXECUTORS can be set to specify the number of parallel executors:

```
export NUM_EXECUTORS=8
cat commands.txt | pxe
```

## License

This software is released under the BSD 2-Clause License. See the LICENSE file for more details.

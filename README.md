# peeve

> My pet peeve: Wrangling with virtual environments for simple scripts.

peeve provides a virtual environment and runs your script in a single command:

```sh
peeve script.py
```

or with the shorter alias:

```sh
pv script.py
```

In detail, peeve will:
- Search for a `requirements.txt`
- Create a virtual environment, if required
- Update the installed packages, if required
- Activate the virtual environment, if required
- Run the script

Alternatively, you can add 

```py
from peeve import bootstrap
```

before any third-party import and run the script the usual way:

```sh
python script.py
```


## Motivation

In our team we often provide Python scripts with our internal Git repositories 
to automate any kind of workflow.
As soon as the scripts rely on third-party packages, things start to get complicated.

We all know that you shouldn't install Python packages globally.
However, creating virtual environment, activating it, and keeping the dependencies
up to date are a few steps too many if you just want to run a script.
You can easily forget to update the dependencies after a `git pull`, 
or to activate the virtual environment when you start a new shell session.
Even worse, the commands for activation depend on your shell and operating system.

While there are excellent tools like pipx, they typically require you to package 
your scripts.
Especially for team members who are not Python experts because they develop in
other languages are have other roles such as testers, this situation is challenging.


## Installation

peeve is available on the Python Package Index:

```sh
pip install peeve
```

Since peeve does not have any third-party dependencies, a global installation
is probably less harmful than usually.
Still, you should prefer pipx if you only need the command line usage: 

```sh
pipx install peeve
```

Since peeve is a single file with no dependencies, you can easily copy it into
you project ("vendoring") or use a similar mechanism like Git subtrees or Git submodules.


## Usage

### Command line

Assuming you have a project with the following files:

```
script.py
requirements.txt
...
```

Use `peeve` instead of `python` to run your script:

```sh
peeve script.py
```

You may also use the shorter `pv` alias:

```sh
pv script.py
```

If the `peeve` command is not accesible, use:

```sh
python -m peeve script.py
```

It will:
- Create a virtual environment `.venv`, if not available.
- Install the `requirements.txt`, if not up to date.
- Pass the remaining arguments to the python interpreter of the venv.

If there is nothing to do, the startup is not much slower than the Python interpreter itself.


### API

Add a single import line to your script:

```py
# standard library imports

from peeve import bootstrap

# third-party imports
```

Then you can execute the script directly with the Python interpreter: 

```sh
python script.py
```

You may need to replace `python` by the appropriate command on your system.
In any case, Python must be able to import `peeve`, so you must have it installed
globally, inside the current virtual environment, or have the `peeve.py` script on
the Python search path.

### Advanced

#### Python version

peeve uses the Python interpreter it was invoked with.
You can combine the Python launcher with peeve to select the desired Python version:

```sh
py -3.10 -m peeve script.py
```

Currently, peeve does not check the Python version in any way.
If you call peeve with a different Pythin version than the one you used to create
the virtual environment, you may encounter problems.
In this case, delete the virtual environment and let peeve recreate it.

#### Compatibility with pip and venv

peeve uses pip and venv and is fully compatible to direct usage of those tools.
This means that peeve can update and activate manually created virtual
envionments, or that you can manually modify virtual environments created with
peeve. However, peeve cannot detect such changes since they pypass the
hashing mechanism.

peeve makes to assumptions about your project:
1. you have a `requirements.txt` at the root of the project
2. you want to use a virtual environment `.venv` at the root of the project

Other requirement files or virtual environments are ignored.

#### Active virtual environments

You may use peeve from within an active virtual environment.
If the active environment is the desired `.venv` one, peeve will continue to use it.
If it is a different one, peeve will switch to `.venv` automatically.


## Features

Implemented:
- [X] Single file, no external dependencies
- [X] No configuration required
- [X] No packaging of scripts required
- [X] Dual usage: from command line or as import 
- [X] Dicovery of `requirements.txt` and existing `.venv` in parent directory
- [X] Hashing of requirements to skip unnecessary upgrade
- [X] Fast in-process venv activation and script execution

Planned:
- [ ] Awareness of parallel Python versions and/or operating systems
- [ ] Support for other interpreter modes (e.g. `-m`, `-c` or interactive)
- [ ] Configuration of requirements file location and/or venv location
- [ ] Support for other dependency specification formats


## Alternatives

### Tox

`tox` is a much more powerful tool that can achieve a similar effect
if you invoke `tox -- script.py` with the following `tox.ini`:

```ini
[testenv]
skip_install = true
deps = -r requirements.txt
commands = python {posargs}
```

`peeve` is faster and works without any configuration.


## TODO

- [ ] Generate code coverage report 
- [ ] Generate HTML documentation
- [ ] Setup CI


## Changelog

### v0.2.0 (2022-04-23)

- Fix broken packaging
- Fix Linux/MacOS support
- Fix Python 3.7 support

### v0.1.0 (2022-04-23)

- Initial release


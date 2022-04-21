# peeve

> Script launcher with automatic installation of dependencies

Imagine you have project with a bunch of Python scripts that require additional packages.
As a good citizen, you create a virtual environment, install the dependencies,
always remember to activate the virtual environment and update the dependencies whenever they change.
But you just want to execute the scripts, right? That's what `peeve` is good for!
Use `peeve script.py` and it will do all the extra steps in the background for you!

Features:
- Zero configuration.
- Single file, no dependencies - just drop it wherever you need it.
- No need to package your project.
- Parallel Windows / Linux support, e.g. for WSL.
- Hashing of requirements for quick startup.

The name `peeve` contains the letters "p" for `python`, `project` and `pip`,
and "v" for `venv`.
It also alludes to the annoyance virtual environment management.
According to Google, a pet peeve is

> something that a particular person finds especially annoying.

## Installation

```sh
$ pip install peeve
```

```sh
$ pipx install peeve
```

## Usage

Assuming you have a project with the following files:

```
script.py
requirements.txt
...
```

Use `peeve` instead of `python` to run your script:

```sh
$ peeve script.py
```

If the `peeve` command is not accesible, use:

```sh
$ python -m peeve script.py
```

It will:
- Create a virtual environment `.venv`, if not available.
- Install the `requirements.txt`, if not up to date.
- Pass the remaining arguments to the python interpreter of the venv.

If there is nothing to do, the startup is not much slower than the Python interpreter itself.

### API

Create virtual environment and restart script, if necessary:

```py
import peeve; peeve.main()  # noqa
```


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


## Design

- Two modes of usage: as launcher and as import package
- As module: `import peeve; peeve.bootstrap()`
- As console scripts: `peeve script.py`
  - Works as drop-in replacement for python interpreter
- Principles:
  - Single file
  - No external dependencies
  - No configuration
- Assumptions:
  - Use requirements.txt (can later be extended)
  - virtual environment at root called `venv`
  - Allow access to same project with different shells or shared folder from
- Configuration:
  - Hierarchy: command line options, environment variables, configuration file


## Features

### Planned

- [ ] Multi-homing (multile Python versions and/or operating systems)
- [ ] Configuration of requirements location and/or venv location
- [ ] Programmatic usage: nice way for import without function call


# TODO

- [ ] Error handling
- [ ] Make dynamic import 
- [ ] Make initial commit
- [ ] Write tests
- [ ] Set up CI
- [ ] Write documentation
- [ ] Make initial release

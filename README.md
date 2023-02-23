# jansiexkernel

![alt](jansiexkernel/logo-svg.svg)

A simple iex/elixir kernel for jupyter.
Created using IPython's kernel and pexpect's REPLWrapper subclasses.
This is a WIP, some things might just not work.

## Dev Installation

- install Elixir from your distro's package manager
- `pip install` jupyterlab and pexpect
- download/clone this project
- open shell in project folder
- `pip install -e ./`
- `jupyter kernelspec install --user jansiexkernel`

## Uninstall

- `jupyter kernelspec uninstall jansiexkernel`
- `pip uninstall jansiexkernel`

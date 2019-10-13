# Handsdown: Cli parser

- [Handsdown: Cli parser](#handsdown-cli-parser)
  - [abs_path](#abs_path)
  - [get_cli_parser](#get_cli_parser)

> Auto-generated documentation for [handsdown.cli_parser](..//home/vlad/work/vemel/handsdown/handsdown/cli_parser.py) module.

## abs_path

[🔍 find in source code](../handsdown/cli_parser.py#L6)

```python
def abs_path(path: str) -> pathlib.Path
```
Make path absolute.

#### Arguments

path - A path to check.

#### Returns

An absolute path.

## get_cli_parser

[🔍 find in source code](../handsdown/cli_parser.py#L19)

```python
def get_cli_parser() -> argparse.ArgumentParser
```
Get CLI arguments parser.

#### Returns

An `argparse.ArgumentParser` instance.
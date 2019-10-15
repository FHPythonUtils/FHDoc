# Utils

- [Handsdown](./README.md) / [Handsdown](./handsdown_index.md) / Utils
  - [OSEnvironMock](#osenvironmock)
  - [get_title_from_path_part](#get_title_from_path_part)

> Auto-generated documentation for [handsdown.utils](../handsdown/utils.py) module.

## OSEnvironMock

[🔍 find in source code](../handsdown/utils.py#L5)

```python
class OSEnvironMock(*args, **kwargs)
```

Mock for `os.environ` that returns `env` string isntead of undefined variables.

## get_title_from_path_part

[🔍 find in source code](../handsdown/utils.py#L14)

```python
def get_title_from_path_part(path_part: str) -> str
```

Convert `pathlib.Path` part to a human-readable title.
Replace underscores with spaces and capitalize result.

#### Arguments

- `path_part` - Part of filename path.

#### Returns

A human-readable title as a string.

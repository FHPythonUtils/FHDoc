# Loader

> Auto-generated documentation for [loader](../loader.py) module..

Loader for python source code.

- [Index](README.md#modules) / Loader
  - [Loader](#loader)
    - [Loader().get_import_string](#loaderget_import_string)
    - [Loader().get_module_record](#loaderget_module_record)
    - [Loader.get_source_line_number](#loaderget_source_line_number)
    - [Loader().import_module](#loaderimport_module)
    - [Loader().setup](#loadersetup)
  - [LoaderError](#loadererror)

## Loader

[🔍 find in source code](../loader.py#L36)

```python
class Loader(
    root_path: Path,
    output_path: Path,
    logger: logging.Logger,
) -> None
```

Loader for python source code.

#### Examples

```python
loader = Loader(Path('path/to/my_module/'))
my_module_utils = loader.import_module('my_module.utils')
```

#### Arguments

- `root_path` - Root path of the project.
- `output_path` - Docs output path.
- `logger` - Logger instance.

### Loader().get_import_string

[🔍 find in source code](../loader.py#L209)

```python
def get_import_string(source_path: Path) -> Text
```

Get Python import string for a source `source_path` relative to `root_path`.

#### Returns

A Python import string.

#### Examples

```python
loader = Loader(root_path=Path("/root"), ...)
loader.get_import_string('/root/my_module/test.py')
'my_module.test'

loader.get_import_string('/root/my_module/__init__.py')
'my_module'
```

#### Arguments

- `source_path` - Path to a source file.

### Loader().get_module_record

[🔍 find in source code](../loader.py#L97)

```python
def get_module_record(source_path: Path) -> Optional[ModuleRecord]
```

Build [ModuleRecord](module_record.md#modulerecord) for given `source_path`.

#### Returns

A new [ModuleRecord](module_record.md#modulerecord) instance or None if there is ntohing to import.

#### Arguments

- `source_path` - Absolute path to source file.

#### Raises

- [LoaderError](#loadererror) - If module or any of it's objects cannot be imported.

### Loader.get_source_line_number

[🔍 find in source code](../loader.py#L494)

```python
def get_source_line_number(obj: Any) -> int
```

Get line number in source file where `obj` is declared.

- `obj` - Object to inspect.

#### Returns

A line number as an integer, starting for 1.

### Loader().import_module

[🔍 find in source code](../loader.py#L239)

```python
def import_module(file_path: Path) -> Any
```

Import module using `import_paths` list. Clean up all patches afterwards.

- Patch `sys.path` to add current repo to it.
- Patch `os.environ` to avoid failing on undefined variables.
- Patch `typing.TYPE_CHECKING` to `True`.
- Patch `logging.Logger`.
- Patch `logging.config.dictConfig`.

#### Returns

Imported module object.

#### Arguments

- `file_path` - Abslute path to source file.

### Loader().setup

[🔍 find in source code](../loader.py#L69)

```python
def setup() -> None
```

Setup local frameworks if needed.

Frameworks supported:
- `Django` (if `DJANGO_SETTINGS_MODULE` env variable is defined)

## LoaderError

[🔍 find in source code](../loader.py#L30)

```python
class LoaderError()
```

Main error for [Loader](#loader) class.

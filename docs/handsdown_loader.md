# Handsdown: Loader

- [Handsdown: Loader](#handsdown-loader)
  - [Loader](#loader)
    - [Loader()._discover_module_objects](#loader_discover_module_objects)
    - [Loader()._get_object_docstring](#loader_get_object_docstring)
    - [Loader().get_module_record](#loaderget_module_record)
    - [Loader.get_object_signature](#loaderget_object_signature)
    - [Loader.get_source_line_number](#loaderget_source_line_number)
    - [Loader().import_module](#loaderimport_module)
    - [Loader().setup](#loadersetup)
  - [LoaderError](#loadererror)

> Auto-generated documentation for [handsdown.loader](../handsdown/loader.py) module.

## Loader

[🔍 find in source code](../handsdown/loader.py#L23)

```python
class Loader(root_path: pathlib.Path, logger: logging.Logger)
```

Loader for python source code.

#### Examples

```python
loader = Loader(Path('path/to/my_module/'))
my_module_utils = loader.import_module('my_module.utils')
```

#### Arguments

- `import_paths` - List of import paths for `import_module` lookup.

### Loader()._discover_module_objects

[🔍 find in source code](../handsdown/loader.py#L272)

```python
def _discover_module_objects(
    module_record: handsdown.module_record.ModuleRecord,
) -> Generator[handsdown.module_record.ModuleObjectRecord, NoneType, NoneType]
```

Get `ModuleObjectRecord` for every object in a module.

#### Arguments

- `module_record` - `ModuleRecord` instance.

#### Returns

A generator that yields `ModuleObjectRecord` instances.

#### See also

- [ModuleRecord](./handsdown_module_record.md#modulerecord)
- [ModuleObjectRecord](./handsdown_module_record.md#moduleobjectrecord)

### Loader()._get_object_docstring

[🔍 find in source code](../handsdown/loader.py#L167)

```python
def _get_object_docstring(obj: Any) -> str
```

Get trimmed object docstring or an empty string.

#### Arguments

- `obj` - Object to inspect.

#### Returns

A string with object docsting.

### Loader().get_module_record

[🔍 find in source code](../handsdown/loader.py#L78)

```python
def get_module_record(
    source_path: pathlib.Path,
) -> Union[handsdown.module_record.ModuleRecord, NoneType]
```

Build `ModuleRecord` for given `source_path`.

#### Arguments

- `source_path` - Absolute path to source file.

#### Returns

A new `ModuleRecord` instance or None if there is ntohing to import.

#### Raises

- [LoaderError](#loadererror) - If module or any of it's objects cannot be imported.

#### See also

- [ModuleRecord](./handsdown_module_record.md#modulerecord)

### Loader.get_object_signature

[🔍 find in source code](../handsdown/loader.py#L150)

```python
def get_object_signature(obj: Any) -> Union[str, NoneType]
```

Get class, method or function signature. If object is not callable -
returns None.

#### Arguments

- `obj` - Object to inspect.

#### Returns

A string with object signature or None.

### Loader.get_source_line_number

[🔍 find in source code](../handsdown/loader.py#L343)

```python
def get_source_line_number(obj: Any) -> int
```

Get line number in source file where `obj` is declared.

- `obj` - Object to inspect.

#### Returns

A line number as an integer, starting for 1.

### Loader().import_module

[🔍 find in source code](../handsdown/loader.py#L208)

```python
def import_module(file_path: pathlib.Path) -> Any
```

Import module using `import_paths` list. Clean up all patches afterwards.

- Patch `sys.path` to add current repo to it.
- Patch `os.environ` to avoid failing on undefined variables.
- Patch `typing.TYPE_CHECKING` to `True`.

#### Arguments

- `file_path` - Abslute path to source file.

#### Returns

Imported module object.

### Loader().setup

[🔍 find in source code](../handsdown/loader.py#L51)

```python
def setup() -> None
```

Setup local frameworks if needed.

Frameworks supported:
- `Django` (if `DJANGO_SETTINGS_MODULE` env variable is defined)

## LoaderError

[🔍 find in source code](../handsdown/loader.py#L17)

```python
class LoaderError(*args, **kwargs)
```

Main error for [Loader](#loader) class.

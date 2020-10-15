# Utils

> Auto-generated documentation for [fhdoc.utils](../../../fhdoc/utils/__init__.py) module.

Handful utils that do not deserve a separate module.

- [Fhdoc](../../README.md#fhdoc-index) / [Modules](../../MODULES.md#modules) / [Fhdoc](../index.md#fhdoc) / Utils
    - [extract_md_title](#extract_md_title)
    - [make_title](#make_title)
    - [render_asset](#render_asset)
    - Modules
        - [DocstringFormatter](docstring_formatter.md#docstringformatter)
        - [ImportString](import_string.md#importstring)
        - [IndentTrimmer](indent_trimmer.md#indenttrimmer)
        - [Logger](logger.md#logger)
        - [PathFinder](path_finder.md#pathfinder)

## extract_md_title

[[find in source code]](../../../fhdoc/utils/__init__.py#L66)

```python
def extract_md_title(content: Text) -> Tuple[Text, Text]:
```

Extract title from the first line of content.
If title is present -  return a title and a remnaing content.
if not - return an empty title and untouched content.

#### Examples

```python
extract_md_title('# Title\ncontent')
('Title', 'content')

extract_md_title('no title\ncontent')
('', 'no title\ncontent')
```

#### Returns

A tuple fo title and remaining content.

## make_title

[[find in source code]](../../../fhdoc/utils/__init__.py#L11)

```python
def make_title(file_stem: Text) -> Text:
```

Convert `pathlib.Path` part or any other string to a human-readable title.
Replace underscores with spaces and capitalize result.

#### Examples

```python
make_title(Path("my_module/my_path.py").stem)
"My Path"

make_title("my_title")
"My Title"

make_title("__init__.py")
"Init Py"

make_title(Path("my_module/__main__.py").stem)
"Module"
```

#### Arguments

- `file_stem` - Stem from path.

#### Returns

A human-readable title as a string.

## render_asset

[[find in source code]](../../../fhdoc/utils/__init__.py#L51)

```python
def render_asset(
    name: Text,
    target_path: Path,
    format_dict: Dict[Text, Text],
) -> None:
```

Render `assets/<name>` file to `target_path`.

#### Arguments

- `name` - Asset file name.
- `target_path` - Path of output file.
- `format_dict` - Format asset with values from the dict before writing.

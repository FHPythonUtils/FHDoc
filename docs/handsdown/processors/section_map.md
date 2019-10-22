# SectionMap

> Auto-generated documentation for [handsdown.processors.section_map](https://github.com/vemel/handsdown/blob/master/handsdown/processors/section_map.py) module.

Module for splitting docstring into `Section` groups.

- [Handsdown](../../README.md#-handsdown---python-documentation-generator) / [Modules](../../MODULES.md#modules) / [Handsdown](../index.md#handsdown) / [Processors](index.md#processors) / SectionMap
  - [Section](#section)
    - [Section().render](#sectionrender)
  - [SectionBlock](#sectionblock)
    - [SectionBlock().is_code](#sectionblockis_code)
    - [SectionBlock().is_header](#sectionblockis_header)
    - [SectionBlock().render](#sectionblockrender)
  - [SectionMap](#sectionmap)
    - [SectionMap().add_block](#sectionmapadd_block)
    - [SectionMap().add_line](#sectionmapadd_line)
    - [SectionMap().sections](#sectionmapsections)
    - [SectionMap().trim_block](#sectionmaptrim_block)

## Section

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/processors/section_map.py#L48)

```python
class Section():
    def __init__(title: List[SectionBlock], blocks: Text) -> None:
```

Dataclass representing a section in a [SectionMap](#sectionmap).

#### Arguments

- `title` - Section title.
- `blocks` - List of line blocks.

#### See also

- [Section](#section)

### Section().render

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/processors/section_map.py#L62)

```python
def render() -> Text:
```

Render all Section block lines.

#### Returns

Section lines as a text.

## SectionBlock

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/processors/section_map.py#L12)

```python
class SectionBlock():
    def __init__(lines: List[Text]) -> None:
```

Dataclass representing a [Section](#section) block.

#### Arguments

- `lines` - List of lines.

### SectionBlock().is_code

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/processors/section_map.py#L24)

```python
def is_code() -> bool:
```

### SectionBlock().is_header

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/processors/section_map.py#L30)

```python
def is_header() -> bool:
```

### SectionBlock().render

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/processors/section_map.py#L36)

```python
def render() -> Text:
```

Render trimmed block lines.

#### Returns

Block lines as a text.

## SectionMap

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/processors/section_map.py#L77)

```python
class SectionMap(dict):
    def __init__() -> None:
```

Dict-based storage for parsed [Section](#section) list for
[BaseDocstringProcessor](base.md#basedocstringprocessor)

Key is a [Section](#section) title.
Value is a related [Section](#section) instance.

### SectionMap().add_block

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/processors/section_map.py#L114)

```python
def add_block(section_name: Text) -> None:
```

Add new [SectionBlock](#sectionblock) to section `section_name`.
If [Section](#section) does not exist - it is not created.

#### Arguments

- `section_name` - Target section title

### SectionMap().add_line

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/processors/section_map.py#L91)

```python
def add_line(section_name: Text, line: Text) -> None:
```

Add new `line` to the last [SectionBlock](#sectionblock) of section `section_name`.
If line and section are empty - section is not created.

#### Arguments

- `section_name` - Target section title
- `line` - Line to add

### SectionMap().sections

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/processors/section_map.py#L144)

```python
@property
def sections() -> Generator[Section, None, None]:
```

Iterate over existing [Section](#section) objects.

#### Yields

[Section](#section) objects in order of appearance.

#### See also

- [SectionMap().sections](#sectionmapsections)

### SectionMap().trim_block

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/processors/section_map.py#L128)

```python
def trim_block(section_name: Text) -> None:
```

Delete last empty lines from the last [SectionBlock](#sectionblock).
If [Section](#section) does not exist - it is not created.

#### Arguments

- `section_name` - Target section title.

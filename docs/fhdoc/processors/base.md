# base

> Auto-generated documentation for [fhdoc.processors.base](../../../fhdoc/processors/base.py) module.

Base class for all docstring processors:

- [Fhdoc](../../README.md#fhdoc-index) / [Modules](../../README.md#fhdoc-modules) / [fhdoc](../index.md#fhdoc) / [processors](index.md#processors) / base
    - [Links](#links)
    - [Supported features](#supported-features)
    - [BaseDocstringProcessor](#basedocstringprocessor)
        - [BaseDocstringProcessor().build_sections](#basedocstringprocessorbuild_sections)

## Links

- [PEP257DocstringProcessor](pep257.md#pep257docstringprocessor)
- [RSTDocstringProcessor](rst.md#rstdocstringprocessor)
- [SmartDocstringProcessor](smart.md#smartdocstringprocessor)

## Supported features

- `<triple_backticks><?language>` starts a new Markdown-style code block, ended with triple backticks
- `<line>::` starts a new Markdown-style Python code block, ended with unindent
- `<triple_tildes><?language>` starts a new Markdown-style block, ends with `<triple_tildes>`
- `>>>` starts a new Markdown-style Python block, ended with unindent or line not starting with `>>>` or `...`

## BaseDocstringProcessor

[[find in source code]](../../../fhdoc/processors/base.py#L26)

```python
class BaseDocstringProcessor(object):
    def __init__() -> None:
```

Base docstring processor. All docstring processors are based on top of it.

#### Attributes

- `line_re_map` - Mapping of line regexp to format string for it
- `section_name_map` - Mapping of Section search key to Section title
- `replace_map` - Mapping of string to replace to replacer

### BaseDocstringProcessor().build_sections

[[find in source code]](../../../fhdoc/processors/base.py#L66)

```python
def build_sections(content: Text) -> SectionMap:
```

Parse docstring and split it to sections with arrays of strings.

#### Arguments

- `content` - Object docstring.

#### Returns

A dictionary where key is a section name and value is a list of string sof this
section.

#### See also

- [SectionMap](section_map.md#sectionmap)

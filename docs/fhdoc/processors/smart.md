# smart

> Auto-generated documentation for [fhdoc.processors.smart](../../../fhdoc/processors/smart.py) module.

Docstring processor that selects a `DocstringProcessor` based on a docstring content:

- [Fhdoc](../../README.md#fhdoc-index) / [Modules](../../MODULES.md#fhdoc-modules) / [fhdoc](../index.md#fhdoc) / [processors](index.md#processors) / smart
    - [SmartDocstringProcessor](#smartdocstringprocessor)
        - [SmartDocstringProcessor().build_sections](#smartdocstringprocessorbuild_sections)

- [PEP257DocstringProcessor](pep257.md#pep257docstringprocessor)
- [RSTDocstringProcessor](rst.md#rstdocstringprocessor)

## SmartDocstringProcessor

[[find in source code]](../../../fhdoc/processors/smart.py#L20)

```python
class SmartDocstringProcessor(BaseDocstringProcessor):
    def __init__() -> None:
```

Docstring processor that selects a `DocstringProcessor` based on a docstring content.

#### See also

- [BaseDocstringProcessor](base.md#basedocstringprocessor)

### SmartDocstringProcessor().build_sections

[[find in source code]](../../../fhdoc/processors/smart.py#L35)

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

# MDDocument

> Auto-generated documentation for [handsdown.md_document](../../handsdown/md_document.py) module.

- [Index](../README.md#handsdown-index) / [Handsdown](index.md#handsdown) / [MDDocument](#mddocument) / MDDocument
  - [MDDocument](#mddocument)
    - [MDDocument().path](#mddocumentpath)
    - [MDDocument().sections](#mddocumentsections)
    - [MDDocument().subtitle](#mddocumentsubtitle)
    - [MDDocument().title](#mddocumenttitle)
    - [MDDocument().toc_section](#mddocumenttoc_section)
    - [MDDocument().append](#mddocumentappend)
    - [MDDocument().append_title](#mddocumentappend_title)
    - [MDDocument().ensure_toc_exists](#mddocumentensure_toc_exists)
    - [MDDocument.extract_title](#mddocumentextract_title)
    - [MDDocument().generate_toc_section](#mddocumentgenerate_toc_section)
    - [MDDocument.get_anchor](#mddocumentget_anchor)
    - [MDDocument.is_toc](#mddocumentis_toc)
    - [MDDocument().read](#mddocumentread)
    - [MDDocument().render_doc_link](#mddocumentrender_doc_link)
    - [MDDocument.render_link](#mddocumentrender_link)
    - [MDDocument().write](#mddocumentwrite)

## MDDocument

[🔍 find in source code](../../handsdown/md_document.py#l15)

```python
class MDDocument(path: pathlib.Path)
```

MD file wrapper. Controls document title and Table of Contents.
Can be used as a context manager, on exit context is written
to `path`.

#### Examples

```python
md_doc = MDDocument(path=Path('output.md'))
md_doc.append('## New section')
md_doc.append('some content')
md_doc.title = 'My doc'
md_doc.ensure_toc_exists()
md_doc.write()

# output is indented for readability
Path('output.md').read_text()
'''# My doc

- [My doc](#my-doc)
  - [New section](#new-section)

## New section

some content
'''

with MDDocument(path=Path('output.md')) as md_document:
    md_document.title = 'My doc'
    md_doc.append_title('New section', level=2)
    md_doc.append('New line')
```

#### Arguments

- `path` - Path to store document.

### MDDocument().path

[🔍 find in source code](../../handsdown/md_document.py#l15)

```python
#property getter
def path() -> pathlib.Path
```

Output path of the document.

### MDDocument().sections

[🔍 find in source code](../../handsdown/md_document.py#l15)

```python
#property getter
def sections() -> List[str]
```

All non-special `sections` of the document.

### MDDocument().subtitle

[🔍 find in source code](../../handsdown/md_document.py#l15)

```python
#property getter
def subtitle() -> Union[str, NoneType]

#property setter
def subtitle(subtitle: str) -> None
```

### MDDocument().title

[🔍 find in source code](../../handsdown/md_document.py#l15)

```python
#property getter
def title() -> Union[str, NoneType]

#property setter
def title(title: str) -> None
```

### MDDocument().toc_section

[🔍 find in source code](../../handsdown/md_document.py#l15)

```python
#property getter
def toc_section() -> str

#property setter
def toc_section(toc_section: str) -> None
```

### MDDocument().append

[🔍 find in source code](../../handsdown/md_document.py#l261)

```python
def append(content: str) -> None
```

Append `content` to the document.
Handle trimming and sectioning the content and update
`title` and `toc_section` fields.

#### Arguments

- `content` - Text to add.

### MDDocument().append_title

[🔍 find in source code](../../handsdown/md_document.py#l277)

```python
def append_title(title: str, level: int) -> None
```

Append `title` of a given `level` to the document.
Handle trimming and sectioning the content and update
`title` and `toc_section` fields.

#### Arguments

- `title` - Title to add.
- `level` - Title level, number of `#` symbols.

### MDDocument().ensure_toc_exists

[🔍 find in source code](../../handsdown/md_document.py#l103)

```python
def ensure_toc_exists() -> None
```

Check if ToC exists in the document or create one.

### MDDocument.extract_title

[🔍 find in source code](../../handsdown/md_document.py#l332)

```python
def extract_title(content: str) -> Tuple[str, str]
```

Extract title from the first line of content.
If title is present -  return a title and a remnaing content.
if not - return an empty title and untouched content.

#### Examples

```python
MDDocument.extract_title('# Title\ncontent')
('Title', 'content')

MDDocument.extract_title('no title\ncontent')
('', 'no title\ncontent')
```

#### Returns

A tuple fo title and remaining content.

### MDDocument().generate_toc_section

[🔍 find in source code](../../handsdown/md_document.py#l291)

```python
def generate_toc_section(max_depth: int = 3) -> str
```

Generate Table of Contents MD content.

#### Arguments

- `max_depth` - Add headers to ToC only up to this level.

#### Returns

A string with ToC.

### MDDocument.get_anchor

[🔍 find in source code](../../handsdown/md_document.py#l110)

```python
def get_anchor(title: str) -> str
```

Convert title to Github-compatible anchor link.

#### Returns

A test of anchor link.

### MDDocument.is_toc

[🔍 find in source code](../../handsdown/md_document.py#l122)

```python
def is_toc(section: str) -> bool
```

Check if the section is Tree of Contents.

#### Returns

True the section is ToC.

### MDDocument().read

[🔍 find in source code](../../handsdown/md_document.py#l77)

```python
def read() -> None
```

Read and parse content from `path`.

### MDDocument().render_doc_link

[🔍 find in source code](../../handsdown/md_document.py#l161)

```python
def render_doc_link(
    title: str,
    anchor: str = '',
    target_path: Union[pathlib.Path, NoneType] = None,
) -> str
```

Render Markdown link to a local MD document, use relative path as a link.

#### Examples

```python
md_doc = MDDocument(path='/root/parent/doc.md')
MDDocument.render_doc_link('my title', anchor='My anchor', target_path=Path('/root/parent/doc.md')
'[my title](#my-anchor)'

MDDocument.render_doc_link('my title', target_path=Path('/root/parent/other.md'))
'[my title](other.md)'

MDDocument.render_doc_link('my title', anchor='My anchor', target_path=Path('doc.md'))
'[my title](doc.md#my-anchor)'

MDDocument.render_doc_link('my title', anchor='My anchor')
'[my title](#my-anchor)'
```

#### Arguments

- `title` - Link text.
- `anchor` - Unescaped or escaped anchor tag.
- `target_path` - Target MDDocument path.

#### Returns

A string with Markdown link.

### MDDocument.render_link

[🔍 find in source code](../../handsdown/md_document.py#l139)

```python
def render_link(title: str, link: str) -> str
```

Render Markdown link wih escaped title.

#### Examples

```python
MDDocument.render_link('my title', 'doc.md#test')
'[my title](doc.md#test)'

MDDocument.render_link('MyClass.__init__', 'my.md')
'[MyClass.__init__](doc.md#my.md)'
```

#### Arguments

- `title` - Link text.
- `link` - Link target.

#### Returns

A string with Markdown link.

### MDDocument().write

[🔍 find in source code](../../handsdown/md_document.py#l213)

```python
def write() -> None
```

Write MD content to `path`.

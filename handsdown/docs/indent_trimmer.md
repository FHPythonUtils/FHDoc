# IndentTrimmer

> Auto-generated documentation for [indent_trimmer](../indent_trimmer.py) module..

Utility for removing indentation for sections and lines.

- [Index](README.md#modules) / IndentTrimmer
  - [IndentTrimmer](#indenttrimmer)
    - [IndentTrimmer.get_line_indent](#indenttrimmerget_line_indent)
    - [IndentTrimmer.trim_empty_lines](#indenttrimmertrim_empty_lines)
    - [IndentTrimmer.trim_line](#indenttrimmertrim_line)
    - [IndentTrimmer.trim_lines](#indenttrimmertrim_lines)
    - [IndentTrimmer.trim_text](#indenttrimmertrim_text)

## IndentTrimmer

[🔍 find in source code](../indent_trimmer.py#L12)

```python
class IndentTrimmer()
```

Utility for removing indentation for sections and lines.

### IndentTrimmer.get_line_indent

[🔍 find in source code](../indent_trimmer.py#L125)

```python
def get_line_indent(line: Text) -> int
```

Get indent length of the line.

#### Returns

A number of indentation characters in a beginning of the line.

#### Examples

```python
IndentTrimmer.get_line_indent('   test')
3

IndentTrimmer.get_line_indent('test')
0
```

#### Arguments

- `line` - Line of text.

### IndentTrimmer.trim_empty_lines

[🔍 find in source code](../indent_trimmer.py#L17)

```python
def trim_empty_lines(text: Text) -> Text
```

Trim empty lines in the begging and the end of the text.

#### Returns

A stripped string.

#### Examples

```python
text = '\n  \n test\ntest2\n \n '
IndentTrimmer.trim_empty_lines(text)
' test\ntest2'
```

### IndentTrimmer.trim_line

[🔍 find in source code](../indent_trimmer.py#L97)

```python
def trim_line(line: Text, indent: int) -> Text
```

Trim indent from line if it is empty.

#### Returns

A line with removed indent.

#### Examples

```python
IndentTrimmer.trim_line('     test', 2)
'   test'

IndentTrimmer.trim_line('     test', 6)
'test'

IndentTrimmer.trim_line('     test', 1)
'    test'
```

#### Arguments

- `line` - A line of text.

### IndentTrimmer.trim_lines

[🔍 find in source code](../indent_trimmer.py#L60)

```python
def trim_lines(lines: Iterable[Text]) -> List[Text]
```

Trim minimum indent from each line of text.

#### Returns

A list of lines with trimmed indent.

#### Examples

```python
IndentTrimmer.trim_lines([
    '  asd',
    ' asd',
    '   asd',
])
[
    ' asd',
    'asd',
    '  asd',
]
```

#### Arguments

- `lines` - List of lines.

### IndentTrimmer.trim_text

[🔍 find in source code](../indent_trimmer.py#L40)

```python
def trim_text(text: Text) -> Text
```

Trim minimum indent from each line of text.

#### Returns

A text with trimmed indent.

#### Examples

```python
IndentTrimmer.trim_text('  asd\n asd\n   asd\n')
' asd\nasd\n  asd\n'
```

#### Arguments

- `text` - Multiline text.

# Signature

> Auto-generated documentation for [handsdown.signature](../../handsdown/signature.py) module..

Module for function signature generation.

- [Index](../README.md#modules) / [Handsdown](index.md#handsdown) / Signature
  - [Config](#config)
  - [DefaultValue](#defaultvalue)
  - [Parameter](#parameter)
    - [Parameter.create](#parametercreate)
  - [SignatureBuilder](#signaturebuilder)
    - [SignatureBuilder().build](#signaturebuilderbuild)

## Config

[🔍 find in source code](../../handsdown/signature.py#L14)

```python
class Config(*args, **kwargs)
```

Config class to control signature generation.

Attrubutes:
    BREAK_LINES -- True if function parameters should start from a new line.
    MAX_LINE_LENGTH -- Max signature line length: `100`

## DefaultValue

[🔍 find in source code](../../handsdown/signature.py#L27)

```python
class DefaultValue(original: Type)
```

Represent function parameter default value in signature

#### Arguments

- `original` - Original default value.

## Parameter

[🔍 find in source code](../../handsdown/signature.py#L53)

```python
class Parameter(name: str, kind: Any, default: Type, annotation: Union[Type, NoneType])
```

Represent function parameters in signature

### Parameter.create

[🔍 find in source code](../../handsdown/signature.py#L97)

```python
def create(
    parameter: inspect.Parameter,
    type_hint: Union[Type, NoneType],
) -> handsdown.signature.Parameter
```

Create `ProxyParameter` for original `inspect.Parameter`

#### Arguments

- `parameter` - original `inspect.Parameter`
- `type_hint` - resoled type hint that should replace a lazy annotation

#### See also

- [Parameter](#parameter)

## SignatureBuilder

[🔍 find in source code](../../handsdown/signature.py#L116)

```python
class SignatureBuilder(obj: Any)
```

Renderer for object signature. Support lazy type annotations and tries
to beautify result by splitting lines.

#### Arguments

- `obj` - Object to inspect.

### SignatureBuilder().build

[🔍 find in source code](../../handsdown/signature.py#L173)

```python
def build() -> str
```

Render signature to string.

#### Returns

A string with functions signature.

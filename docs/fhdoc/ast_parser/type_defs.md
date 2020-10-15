# Type Defs

> Auto-generated documentation for [fhdoc.ast_parser.type_defs](../../../fhdoc/ast_parser/type_defs.py) module.

Different AST-related types collection.

- [Fhdoc](../../README.md#fhdoc-index) / [Modules](../../MODULES.md#modules) / [Fhdoc](../index.md#fhdoc) / [AST Parser](index.md#ast-parser) / Type Defs

#### Attributes

- `RenderExpr` - Ready for render expression: `Union[(NodeRecord, Text, RenderPart)]`
- `Node` - AST node or text: `Union[(Text, ast.AST)]`
- `DirtyRenderExpr` - Not ready for render expression, AST has to be wrapped: `Union[(ast.AST, Text, RenderPart)]`
- `ASTIterable` - Iterable AST types: `Union[(ast.List, ast.Set, ast.Tuple)]`
- `ASTImport` - AST import node: `Union[(ast.Import, ast.ImportFrom)]`
- `ASTFunctionDef` - AST import node: `Union[(ast.FunctionDef, ast.AsyncFunctionDef)]`

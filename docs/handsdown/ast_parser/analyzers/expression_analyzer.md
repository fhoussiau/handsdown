# ExpressionAnalyzer

> Auto-generated documentation for [handsdown.ast_parser.analyzers.expression_analyzer](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py) module.

AST analyzer for `ast.expr` records.

- [Handsdown](../../../README.md#-handsdown---python-documentation-generator) / [Modules](../../../MODULES.md#modules) / [Handsdown](../../index.md#handsdown) / [AST Parser](../index.md#ast-parser) / [Analyzers](index.md#analyzers) / ExpressionAnalyzer
    - [ExpressionAnalyzer](#expressionanalyzer)
        - [ExpressionAnalyzer().generic_visit](#expressionanalyzergeneric_visit)
        - [ExpressionAnalyzer().visit_Attribute](#expressionanalyzervisit_attribute)
        - [ExpressionAnalyzer().visit_Await](#expressionanalyzervisit_await)
        - [ExpressionAnalyzer().visit_BinOp](#expressionanalyzervisit_binop)
        - [ExpressionAnalyzer().visit_BoolOp](#expressionanalyzervisit_boolop)
        - [ExpressionAnalyzer().visit_Bytes](#expressionanalyzervisit_bytes)
        - [ExpressionAnalyzer().visit_Call](#expressionanalyzervisit_call)
        - [ExpressionAnalyzer().visit_Compare](#expressionanalyzervisit_compare)
        - [ExpressionAnalyzer().visit_Dict](#expressionanalyzervisit_dict)
        - [ExpressionAnalyzer().visit_DictComp](#expressionanalyzervisit_dictcomp)
        - [ExpressionAnalyzer().visit_Ellipsis](#expressionanalyzervisit_ellipsis)
        - [ExpressionAnalyzer().visit_FormattedValue](#expressionanalyzervisit_formattedvalue)
        - [ExpressionAnalyzer().visit_GeneratorExp](#expressionanalyzervisit_generatorexp)
        - [ExpressionAnalyzer().visit_IfExp](#expressionanalyzervisit_ifexp)
        - [ExpressionAnalyzer().visit_Index](#expressionanalyzervisit_index)
        - [ExpressionAnalyzer().visit_JoinedStr](#expressionanalyzervisit_joinedstr)
        - [ExpressionAnalyzer().visit_Lambda](#expressionanalyzervisit_lambda)
        - [ExpressionAnalyzer().visit_List](#expressionanalyzervisit_list)
        - [ExpressionAnalyzer().visit_ListComp](#expressionanalyzervisit_listcomp)
        - [ExpressionAnalyzer().visit_Name](#expressionanalyzervisit_name)
        - [ExpressionAnalyzer().visit_NameConstant](#expressionanalyzervisit_nameconstant)
        - [ExpressionAnalyzer().visit_Num](#expressionanalyzervisit_num)
        - [ExpressionAnalyzer().visit_Set](#expressionanalyzervisit_set)
        - [ExpressionAnalyzer().visit_SetComp](#expressionanalyzervisit_setcomp)
        - [ExpressionAnalyzer().visit_Slice](#expressionanalyzervisit_slice)
        - [ExpressionAnalyzer().visit_Starred](#expressionanalyzervisit_starred)
        - [ExpressionAnalyzer().visit_Str](#expressionanalyzervisit_str)
        - [ExpressionAnalyzer().visit_Subscript](#expressionanalyzervisit_subscript)
        - [ExpressionAnalyzer().visit_Tuple](#expressionanalyzervisit_tuple)
        - [ExpressionAnalyzer().visit_UnaryOp](#expressionanalyzervisit_unaryop)
        - [ExpressionAnalyzer().visit_Yield](#expressionanalyzervisit_yield)
        - [ExpressionAnalyzer().visit_YieldFrom](#expressionanalyzervisit_yieldfrom)
        - [ExpressionAnalyzer().visit_arg](#expressionanalyzervisit_arg)
        - [ExpressionAnalyzer().visit_arguments](#expressionanalyzervisit_arguments)
        - [ExpressionAnalyzer().visit_comprehension](#expressionanalyzervisit_comprehension)
        - [ExpressionAnalyzer().visit_keyword](#expressionanalyzervisit_keyword)

## ExpressionAnalyzer

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L13)

```python
class ExpressionAnalyzer(BaseAnalyzer):
    def __init__() -> None:
```

AST analyzer for `ast.expr` records.

Prepares `parts` for `NodeRecord.render` method.

#### Attributes

- `UNKNOWN` - dummy value to replace unknown nodes and operators: `'...'`

#### See also

- [BaseAnalyzer](base_analyzer.md#baseanalyzer)

### ExpressionAnalyzer().generic_visit

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L782)

```python
def generic_visit(node: ast.AST) -> None:
```

Parse info from an unknown `ast.AST` node and put `...` to `parts`.

Logs warning with node class.

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_Attribute

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L164)

```python
def visit_Attribute(node: ast.Attribute) -> None:
```

Parse info from `ast.Attribute` node and put it to `parts`.

#### Examples

```python
my_object.attribute
```

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_Await

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L737)

```python
def visit_Await(node: ast.Await) -> None:
```

Parse info from `ast.Await` node and put it to `parts`.

#### Examples

```python
await result
```

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_BinOp

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L389)

```python
def visit_BinOp(node: ast.BinOp) -> None:
```

Parse info from `ast.BinOp` node and put it to `parts`.

#### Examples

```python
1 + 5
value + 1
```

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_BoolOp

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L410)

```python
def visit_BoolOp(node: ast.BoolOp) -> None:
```

Parse info from `ast.BoolOp` node and put it to `parts`.

#### Examples

```python
value or True
a and b
```

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_Bytes

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L85)

```python
def visit_Bytes(node: ast.Bytes) -> None:
```

Parse info from `ast.Bytes` node and put it to `parts`.

#### Examples

```python
b"my_string"
```

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_Call

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L253)

```python
def visit_Call(node: ast.Call) -> None:
```

Parse info from `ast.Call` node and put it to `parts`.

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_Compare

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L366)

```python
def visit_Compare(node: ast.Compare) -> None:
```

Parse info from `ast.Compare` node and put it to `parts`.

#### Examples

```python
value < 5
1 < weekday < 7
```

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_Dict

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L342)

```python
def visit_Dict(node: ast.Dict) -> None:
```

Parse info from `ast.Dict` node and put it to `parts`.

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_DictComp

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L646)

```python
def visit_DictComp(node: ast.DictComp) -> None:
```

Parse info from `ast.DictComp` node and put it to `parts`.

#### Examples

```python
{k: 1 for k in range(3)}
```

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_Ellipsis

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L553)

```python
def visit_Ellipsis(_node: ast.ASTEllipsis) -> None:
```

Parse info from `ast.Ellipsis` node and put it to `parts`.

#### Examples

```python
...
```

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_FormattedValue

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L612)

```python
def visit_FormattedValue(node: ast.FormattedValue) -> None:
```

Parse info from `ast.FormattedValue` node and put it to `parts`.

#### Examples

```python
f"{formatted_value}"
```

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_GeneratorExp

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L702)

```python
def visit_GeneratorExp(node: ast.GeneratorExp) -> None:
```

Parse info from `ast.GeneratorExp` node and put it to `parts`.

#### Examples

```python
(k + 1 for k in range(3))
```

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_IfExp

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L720)

```python
def visit_IfExp(node: ast.IfExp) -> None:
```

Parse info from `ast.IfExp` node and put it to `parts`.

#### Examples

```python
5 if my_value else 6
```

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_Index

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L536)

```python
def visit_Index(node: ast.Index) -> None:
```

Parse info from `ast.Index` node and put it to `parts`.

#### Examples

```python
Union[str, bool]
Union[str]
```

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_JoinedStr

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L590)

```python
def visit_JoinedStr(node: ast.JoinedStr) -> None:
```

Parse info from `ast.JoinedStr` node and put it to `parts`.

#### Examples

```python
f'str: {my_string}'
```

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_Lambda

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L454)

```python
def visit_Lambda(node: ast.Lambda) -> None:
```

Parse info from `ast.Lambda` node and put it to `parts`.

#### Examples

```python
lambda x: x + 5
```

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_List

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L208)

```python
def visit_List(node: ast.List) -> None:
```

Parse info from `ast.List` node and put it to `parts`.

#### Examples

```python
[1, 2, 3]
```

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_ListComp

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L666)

```python
def visit_ListComp(node: ast.ListComp) -> None:
```

Parse info from `ast.ListComp` node and put it to `parts`.

#### Examples

```python
[k + 1 for k in range(3)]
```

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_Name

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L114)

```python
def visit_Name(node: ast.Name) -> None:
```

Parse info from `ast.Name` node and put it to `parts`.

#### Examples

```python
my_value
```

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_NameConstant

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L128)

```python
def visit_NameConstant(node: ast.NameConstant) -> None:
```

Parse info from `ast.NameConstant` node and put it to `parts`.

#### Examples

```python
None
True
```

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_Num

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L99)

```python
def visit_Num(node: ast.Num) -> None:
```

Parse info from `ast.Num` node and put it to `parts`.

#### Examples

```python
123
123.456
```

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_Set

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L223)

```python
def visit_Set(node: ast.Set) -> None:
```

Parse info from `ast.Set` node and put it to `parts`.

#### Examples

```python
{1, 2, 3}
```

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_SetComp

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L684)

```python
def visit_SetComp(node: ast.SetComp) -> None:
```

Parse info from `ast.SetComp` node and put it to `parts`.

#### Examples

```python
{k + 1 for k in range(3)}
```

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_Slice

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L566)

```python
def visit_Slice(node: ast.Slice) -> None:
```

Parse info from `ast.Slice` node and put it to `parts`.

#### Examples

```python
[1:]
[:2]
[1:2]
[1:2:-1]
[::-1]
```

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_Starred

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L307)

```python
def visit_Starred(node: ast.Starred) -> None:
```

Parse info from `ast.Starred` node and put it to `parts`.

#### Examples

```python
*arg
```

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_Str

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L69)

```python
def visit_Str(node: ast.Str) -> None:
```

Parse info from `ast.Str` node and put it to `parts`.

#### Examples

```python
"my_string"
```

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_Subscript

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L142)

```python
def visit_Subscript(node: ast.Subscript) -> None:
```

Parse info from `ast.Subscript` node and put it to `parts`.

Type annotations are also matched by this method.

#### Examples

```python
Union[Name, bool]
list[1:4]
```

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_Tuple

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L238)

```python
def visit_Tuple(node: ast.Tuple) -> None:
```

Parse info from `ast.Tuple` node and put it to `parts`.

#### Examples

```python
(1, 2, 3)
```

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_UnaryOp

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L432)

```python
def visit_UnaryOp(node: ast.UnaryOp) -> None:
```

Parse info from `ast.UnaryOp` node and put it to `parts`.

#### Examples

```python
+5
-12
~1
not True
```

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_Yield

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L751)

```python
def visit_Yield(node: ast.Yield) -> None:
```

Parse info from `ast.Yield` node and put it to `parts`.

#### Examples

```python
yield
yield value
```

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_YieldFrom

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L768)

```python
def visit_YieldFrom(node: ast.YieldFrom) -> None:
```

Parse info from `ast.YieldFrom` node and put it to `parts`.

#### Examples

```python
yield from my_generator
```

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_arg

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L519)

```python
def visit_arg(node: ast.arg) -> None:
```

Parse info from `ast.arg` node and put it to `parts`.

#### Examples

```python
def my_func(arg)
def my_func(arg: str)
```

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_arguments

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L470)

```python
def visit_arguments(node: ast.arguments) -> None:
```

Parse info from `ast.arguments` node and put it to `parts`.

#### Examples

```python
def my_func(arg, *args, **kwargs)
```

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_comprehension

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L627)

```python
def visit_comprehension(node: ast.comprehension) -> None:
```

Parse info from `ast.comprehension` node and put it to `parts`.

#### Examples

```python
for k in range(3) if k > 0 if True
```

#### Arguments

- `node` - AST node.

### ExpressionAnalyzer().visit_keyword

[[find in source code]](https://github.com/vemel/handsdown/blob/main/handsdown/ast_parser/analyzers/expression_analyzer.py#L321)

```python
def visit_keyword(node: ast.keyword) -> None:
```

Parse info from `ast.keyword` node and put it to `parts`.

#### Examples

```python
my_func(**{"kwarg": "value"})
my_func(kwarg="value")
```

#### Arguments

- `node` - AST node.

# Smart

> Auto-generated documentation for [handsdown.processors.smart](https://github.com/vemel/handsdown/blob/master/handsdown/processors/smart.py) module.

Smart Docstring Processor.

- [Handsdown](../../README.md#-handsdown---python-documentation-generator) / [Modules](../../MODULES.md#modules) / [Handsdown](../index.md#handsdown) / [Processors](index.md#processors) / Smart
    - [SmartDocstringProcessor](#smartdocstringprocessor)
        - [SmartDocstringProcessor().build_sections](#smartdocstringprocessorbuild_sections)

Docstring processor that selects a `DocstringProcessor` based on a docstring content:

- [PEP257DocstringProcessor](pep257.md#pep257docstringprocessor)
- [RSTDocstringProcessor](rst.md#rstdocstringprocessor)

## SmartDocstringProcessor

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/processors/smart.py#L15)

```python
class SmartDocstringProcessor(BaseDocstringProcessor):
    def __init__() -> None:
```

Docstring processor that selects a `DocstringProcessor` based on a docstring content.

#### See also

- [BaseDocstringProcessor](base.md#basedocstringprocessor)

### SmartDocstringProcessor().build_sections

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/processors/smart.py#L28)

```python
def build_sections(content: str) -> SectionMap:
```

Parse docstring and split it to sections with arrays of strings.

#### Arguments

- `content` - Object docstring.

#### Returns

A dictionary where key is a section name and value is a list of string sof this
section.

#### See also

- [SectionMap](section_map.md#sectionmap)

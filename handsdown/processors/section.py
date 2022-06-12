"""
Section in a `SectionMap`.
"""
from typing import Iterable

from handsdown.processors.section_block import SectionBlock


class Section:
    """
    Section in a `SectionMap`.

    Arguments:
        title -- Section title.
        blocks -- List of line blocks.
    """

    def __init__(self, title: str, blocks: Iterable[SectionBlock]) -> None:
        self.title = title
        self.blocks = list(blocks)

    def render(self) -> str:
        """
        Render all Section block lines.

        Returns:
            Section lines as a text.
        """
        result = []
        for block in self.blocks:
            result.append(block.render())

        return "\n\n".join(result)

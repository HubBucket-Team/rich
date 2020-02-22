from typing import Union

from .console import Console, ConsoleOptions, RenderResult
from .style import Style
from .text import Text


class Rule:
    def __init__(
        self,
        title: Union[str, Text] = "",
        character: str = "─",
        style: Union[str, Style] = "rule.line",
    ) -> None:
        """A console renderable to draw a horizontal rule (line).
        
        Args:
            title (str, optional): Text to render in the rule. Defaults to "".
            character (str, optional): Character used to draw the line. Defaults to "─".
        """
        self.title = title
        self.character = character
        self.style = style

    def __repr__(self) -> str:
        return f"Rule({self.title!r}, {self.character!r})"

    def __console__(self, console: Console, options: ConsoleOptions) -> RenderResult:
        width = options.max_width

        if not self.title:
            yield Text(self.character * width, self.style)
        else:
            if isinstance(self.title, Text):
                title_text = self.title
            else:
                title_text = Text.from_markup(self.title, "rule.text")
            if len(title_text) > width - 4:
                title_text.set_length(width - 4)

            rule_text = Text()
            center = (width - len(title_text)) // 2
            rule_text.append(self.character * (center - 1) + " ", self.rule_style)
            rule_text.append(title_text)
            rule_text.append(
                " " + self.character * (width - len(rule_text) - 1), self.rule_style
            )
            yield rule_text


if __name__ == "__main__":
    from .console import Console

    c = Console()

    c.print(Rule())
    c.print(Rule("*Hello, World*"))
    c.print(Rule(Text("Hello, World", "bold red reverse")))
    c.print(Rule("*Hello, World*", character="."))
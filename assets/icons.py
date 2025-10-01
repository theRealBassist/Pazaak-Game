from dataclasses import dataclass
import re

ICONS = {
    "blank_slot": (
                    " _____ ",
                    "|     |",
                    "|     |",
                    "|     |",
                    "|     |",
                    "|_____|",
    ),
    "main_card": (
                    "  ___  ",
                    r" /...\ ",
                    "|.....|",
                    "|.{combined}.|",
                    "|.....|",
                    r" \___/ ",
    ),
    "side_deck": (
                    "  ___  ",
                    r" /...\ ",
                    "|.....|",
                    "|.{combined}.|",
                    "|.....|",
                    r" \___/ ",
    )
}

@dataclass
class Size:
    width: int
    height: int

@dataclass
class Position:
    x: int
    y: int

def renderIcon(name: str, sign: str = ".", value: int = 0) -> list[str]:
    if name in ICONS.keys():
        icon = ICONS[name]
    else:
        raise ValueError("The card's type is not a valid card type")

    sign = str(sign)
    value = str(value)

    combined = f"{sign}{value}"[:3]
    combined  = combined.center(3)
    combined = re.sub(r'\s+', '.', combined)

    lines: list[str] = []
    for line in icon:
        if "{combined}" in line:
            lines.append(line.format(combined=combined))
        else:
            lines.append(line)
    return lines

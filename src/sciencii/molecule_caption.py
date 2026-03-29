"""Draws text captions in science-themed ASCII art styles."""

VALID_STYLES = ("flask", "beaker", "atom", "bond")


def molecule_caption(text, style):
    """Takes a string and a style name, returns ASCII art as a string."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not isinstance(style, str):
        raise TypeError("style must be a string")
    if len(text) == 0:
        raise ValueError("text must not be empty")
    if style not in VALID_STYLES:
        raise ValueError(
            f"style must be one of {VALID_STYLES}, got '{style}'"
        )

    if style == "flask":
        return _flask(text)
    if style == "beaker":
        return _beaker(text)
    if style == "atom":
        return _atom(text)
    return _bond(text)


def _flask(text):
    """Draws text inside an Erlenmeyer flask shape."""
    width = len(text) + 6
    half = width // 2

    lines = []
    neck_pad = half - 1
    lines.append(" " * neck_pad + "||")
    lines.append(" " * neck_pad + "||")

    # sloped sides connecting neck to body
    for i in range(1, half - 1):
        pad = neck_pad - i
        inner = 2 * i
        lines.append(" " * pad + "/" + " " * inner + "\\")

    body_inner = width - 2
    lines.append("/" + text.center(body_inner) + "\\")
    lines.append("+" + "-" * body_inner + "+")

    return "\n".join(lines)


def _beaker(text):
    """Draws text inside a rectangular beaker with a handle."""
    inner_width = len(text) + 4
    lines = []
    lines.append("+" + "-" * inner_width + "+")
    lines.append("|" + " " * inner_width + "|)")
    lines.append("|" + text.center(inner_width) + "|")
    lines.append("|" + " " * inner_width + "|")
    lines.append("+" + "-" * inner_width + "+")
    return "\n".join(lines)


def _atom(text):
    """Wraps text in orbital-looking brackets with a wave underneath."""
    padded = f"  {text}  "
    width = len(padded)
    lines = []
    lines.append(" ." + "-" * width + ".")
    lines.append("({" + padded + "})")
    lines.append(" '" + "-" * width + "'")
    lines.append("  " + "~" * width)
    return "\n".join(lines)


def _bond(text):
    """Puts each character in brackets connected by - and = symbols."""
    if len(text) == 1:
        return f"[{text}]"
    bond_chars = ["-", "=", "-"]
    parts = []
    for i, ch in enumerate(text):
        parts.append(f"[{ch}]")
        if i < len(text) - 1:
            parts.append(bond_chars[i % len(bond_chars)])
    return "".join(parts)
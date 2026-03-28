"""ASCII art DNA helix generator."""


def dna_helix(length: int) -> str:
    """Generate an ASCII art DNA double helix.

    Args:
        length: Number of 5-line cycles to repeat (non-negative integer).

    Returns:
        The ASCII art as a newline-separated string.

    Raises:
        TypeError: If length is not an int or is a bool.
        ValueError: If length is negative.
    """
    if isinstance(length, bool) or not isinstance(length, int):
        raise TypeError("length must be an integer")
    if length < 0:
        raise ValueError("length must be non-negative")
    if length == 0:
        return ""

    lines = []
    for _ in range(length):
        lines.append("O---o")
        lines.append(" O-o")
        lines.append("  O")
        lines.append(" o-O")
        lines.append("o---O")

    return "\n".join(lines)

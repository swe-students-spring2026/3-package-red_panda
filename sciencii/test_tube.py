def test_tube(fill_level, label):
    if not isinstance(fill_level, (int, float)):
        raise TypeError("fill_level must be a number")

    if not isinstance(label, str):
        raise TypeError("label must be a string")

    if fill_level < 0 or fill_level > 100:
        raise ValueError("fill_level must be between 0 and 100")

    height = 10
    filled_rows = round((fill_level / 100) * height)

    lines = []

    for row in range(height):
        if row < height - filled_rows:
            lines.append("|   |")
        else:
            lines.append("|###|")

    lines.append("|___|")
    lines.append(label)

    return "\n".join(lines)


test_tube.__test__ = False
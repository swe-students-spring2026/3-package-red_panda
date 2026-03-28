def pipette(volume, max_volume):
    """
    This function creates an ASCII image of a pipette filled based on volume and max volume.
    """
    if not isinstance(volume, (int, float)):
        raise ValueError("Volume must be a number.")  
    if not isinstance(max_volume, (int, float)):
        raise ValueError("Max volume must be a number.")
    if volume < 0:
        raise ValueError("Volume cannot be negative.")
    if max_volume <= 0:
        raise ValueError("Max volume must be greater than zero.")
    if volume > max_volume:
        raise ValueError("Volume cannot exceed max volume.")   
    # Define dimensions of the pipette
    height = 20
    width = 60
    slope = 0.99

    fill_ratio = volume / max_volume
    filled_levels = int(fill_ratio * height)

    lines = []

    # Body of the pipette
    for i in range(height):
        line = [" "] * width

        center = round(10 + i * slope)

        left = center - 2
        right = center + 2

        # Create the walls of the pipette
        if (0 <= left) and (left < width):
            line[left] = "\\"
        if (0 <= right) and (right < width):
            line[right] = "\\"

        # Fill the pipette with liquid
        if i >= height - filled_levels:
            for j in range(left + 1, right):
                if 0 <= j < width:
                    line[j] = "~"

        # Create graduation marks
        if (height - i) % 5 == 0 and right + 1 < width:
            line[right + 1] = "-"

        lines.append("".join(line))

    # Neck of the pipette:
    for i in range(3):
        line = [" "] * width
        center = int(10 + (height + i) * slope)

        line[center - 1] = "\\"
        line[center + 1] = "\\"
        lines.append("".join(line))

    # Tip of the pipette:
    for i in range(4):
        line = [" "] * width
        center = int(10 + (height + 2 + i) * slope)

        line[center] = "\\"
        lines.append("".join(line))

    # Drop at the tip:
    if volume > 0:
        line = [" "] * width
        center = int(10 + (height + 6) * slope)
        if center < width:
            line[center] = "o"
        lines.append("".join(line))

    # Label how filled the pipette is:
    lines.append(f"\n   {volume}/{max_volume}")

    return "\n".join(lines)
    # End-of-file (EOF)
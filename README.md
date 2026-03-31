# Sciencii

![Build Status](https://github.com/swe-students-spring2026/3-package-red_panda/actions/workflows/build.yml/badge.svg)

A Python package that generates science-themed ASCII art — DNA helices, pipettes, periodic table element cards, test tubes, and molecule-style text captions.

**PyPI:** [https://pypi.org/project/sciencii/](https://pypi.org/project/sciencii/)

## Team

- [Ami](https://github.com/asb9823)
- [Ethan](https://github.com/ethanarnold)
- [Lily](https://github.com/lilylorand)
- [Luca](https://github.com/Landreani04)
- [Rohan](https://github.com/ra4059)

## Installation

```bash
pip install sciencii
```

## Usage

### `dna_helix(length)`

Generates an ASCII DNA double helix. `length` is the number of 5-line cycles to repeat.

```python
from sciencii import dna_helix

print(dna_helix(1))
```

```
O---o
 O-o
  O
 o-O
o---O
```

### `pipette(volume, max_volume)`

Draws an ASCII pipette filled proportionally. `volume` is the current fill level, `max_volume` is the capacity.

```python
from sciencii.pipette import pipette

print(pipette(5, 10))
```

### `get_element(name)`

Looks up an element by name, symbol, or atomic number and shows its ASCII art card. Pass `"table"` for the full periodic table.

```python
import sciencii.periodic_table as periodic_table

periodic_table.get_element("He")
periodic_table.get_element(79)
periodic_table.get_element("table")
```

### `molecule_caption(text, style)`

Draws text in a science-themed ASCII style. `style` can be `"flask"`, `"beaker"`, `"atom"`, or `"bond"`.

```python
from sciencii import molecule_caption

print(molecule_caption("H2O", "flask"))
print(molecule_caption("NaCl", "beaker"))
print(molecule_caption("Fe", "atom"))
print(molecule_caption("CO2", "bond"))
```

### `test_tube(fill_level, label)`

Draws an ASCII test tube filled proportionally. `fill_level` is a number from 0 to 100 representing the percentage filled, and `label` is a string displayed below the tube.

```python
from sciencii import test_tube

print(test_tube(75, "Sample A"))
```

```
|   |
|   |
|   |
|###|
|###|
|###|
|###|
|###|
|###|
|###|
|___|
Sample A
```

## Example Program

See [`example.py`](./example.py) for a runnable program that demonstrates every function.

```bash
python example.py
```

## For Developers

### Setup

Requires Python 3.9+ and [pipenv](https://pipenv.pypa.io/) (`pip install pipenv`).

```bash
git clone https://github.com/swe-students-spring2026/3-package-red_panda.git
cd 3-package-red_panda
pipenv install --dev
```

### Run tests

```bash
pipenv run pytest
```

### Build the package

```bash
pipenv run python -m build
```

### Environment variables

No `.env` file or secret credentials are required to run or test this project.
"""Runnable demo of every sciencii function."""

from sciencii import dna_helix, pipette, get_element, molecule_caption

# DNA Helix
print("DNA Helix (2 cycles)\n")
print(dna_helix(2))

# Pipette
print("\nPipette (5 / 10 mL)\n")
print(pipette(5, 10))

# Element Lookup
print("\nElement Lookup\n")
get_element("He")
get_element(79)

# Molecule Captions
print("\nMolecule Captions\n")
print("Flask:", molecule_caption("H2O", "flask"), sep="\n")
print("\nBeaker:", molecule_caption("NaCl", "beaker"), sep="\n")
print("\nAtom:", molecule_caption("Fe", "atom"), sep="\n")
print("\nBond:", molecule_caption("CO2", "bond"), sep="\n")

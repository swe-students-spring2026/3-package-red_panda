import mendeleev
import sys
from sciencii.periodic_art import elements

def get_art(name):
    #if atomic number, change it to name of element
    name = str(name)
    if name.replace("-", "").isdigit():
        try:
            el_name = mendeleev.element(int(name))
            el_name = el_name.name.lower()
        except:
            print("No element has this atomic number!")
            return None
    #if length is two, it must be a symbol if its a real element (no full names are that size)
    elif len(name) == 2 or len(name) == 1:
        try:
            el_name = mendeleev.element(name.capitalize())
            el_name = el_name.name.lower()
        except:
            print("No element has this symbol!")
            return None
    #otherwise it's either name of element or bad input which will be flagged later
    else:
        el_name = name.lower()
    if el_name not in elements:                
        print("This element doesn't exist!")
        return None
    else:
        print("\n".join(elements.get(el_name)))
        return elements.get(el_name)


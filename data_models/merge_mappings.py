 #!/usr/bin/env python

def merge_mappings():
    """
    Mappings behave like sets in python, which means set
    operations like Union can apply to them.
    Requires Python >= 3.9
    """
    d1 = {'a': 1, 'c': 3}
    d2 = {'a': 2, 'b': 3, 'c': 4}

    # d1 | d2 creates a new dict
    d1_set = d1 | d2
    print(d1_set)

    # d1 |= d2 updates a mapping in place
    print(d1) # d1 was noy changed
    d1 |= d2
    print(d1)

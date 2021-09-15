import string


def join_strings(txt1, txt2) -> string:
    """
    "Join 2 strings, starting with a Capital and seperated by ' '
    Args:
        txt1: the first string to be joined
        txt2: the second string to be joined
    Returns the joined strings, starting with a Capitol and seperated by a ' '
    Raises
        TypeError: if txt1 and/or txt2 is nog a valid string
    """
    # capitalize()
    return txt1.replace(txt1[0], txt1[0].upper()) + " " + txt2.lower()

print('dit', 'is een test')

print(join_strings.__doc__)
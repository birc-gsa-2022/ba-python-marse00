"""Module for computing border arrays."""


def border_array(x: str) -> list[int]:
    """
    Construct the border array for x.

    >>> border_array("aaba")
    [0, 1, 0, 1]
    >>> border_array("ississippi")
    [0, 0, 0, 1, 2, 3, 4, 0, 0, 1]
    >>> border_array("")
    []
    """
    i, j = 0, 1
    ba = [0 for k in range(len(x))]
    while j < len(x):
        if x[i] == x[j]:
            ba[j] = ba[j-1] + 1
            i += 1
        else:
            i = 0
        j += 1

    return ba  # FIXME


def strict_border_array(x: str) -> list[int]:
    """
    Construct the strict border array for x.

    A struct border array is one where the border cannot
    match on the next character. If b is the length of the
    longest border for x[:i+1], it means x[:b] == x[i-b:i+1],
    but for a strict border, it must be the longest border
    such that x[b] != x[i+1].

    >>> strict_border_array("aaba")
    [0, 1, 0, 1]
    >>> strict_border_array("aaaba")
    [0, 0, 2, 0, 1]
    >>> strict_border_array("ississippi")
    [0, 0, 0, 0, 0, 0, 4, 0, 0, 1]
    >>> strict_border_array("")
    []
    """
    ba = border_array(x)
    for i in range(len(ba)):
        if i == 0:
            continue
        if ba[i] != 0:
            ba[i-1] = 0 
    return ba  # FIXME

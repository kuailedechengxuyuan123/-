def calculate(x, y):
    """Calculate according to the specification:

    - if x > 0 and y > 0: return x + y
    - elif x < 0 or y < 0: return x - y
    - else: return 0
    """
    if x > 0 and y > 0:
        return x + y
    elif x < 0 or y < 0:
        return x - y
    else:
        return 0


def linear_search(arr, target, trace=False):
    """Linear search implementation.

    If trace is False (default) returns the index or -1.
    If trace is True returns a tuple: (index, iterations, found)
    which is helpful for testing loop-internal behavior.
    """
    index = -1
    found = False
    i = 0
    n = len(arr)
    iterations = 0
    while i < n and not found:
        iterations += 1
        if arr[i] == target:
            found = True
            index = i
        i += 1

    if trace:
        return index, iterations, found
    return index

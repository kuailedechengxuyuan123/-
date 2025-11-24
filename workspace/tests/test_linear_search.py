from src.math_funcs import linear_search


def test_found_at_start():
    arr = [7, 1, 2]
    assert linear_search(arr, 7) == 0


def test_not_found():
    arr = [1, 2, 3]
    assert linear_search(arr, 4) == -1


def test_trace_middle():
    arr = [10, 20, 30, 40]
    idx, iterations, found = linear_search(arr, 30, trace=True)
    assert idx == 2
    assert found is True
    # loop should have executed 3 times (index 0,1,2)
    assert iterations == 3


def test_trace_not_found_iterations():
    arr = [1, 2, 3]
    idx, iterations, found = linear_search(arr, 99, trace=True)
    assert idx == -1
    assert found is False
    # loop should have executed len(arr) times
    assert iterations == 3

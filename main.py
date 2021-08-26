def sum_of_squares(a):

    sum = 0
    for number in a:
        square = number**2
        sum += square
    return sum


def test_one():
    assert sum_of_squares([1, 2, 3])


def test_two():
    assert sum_of_squares([4, 5, 6])


test_one()
test_two()

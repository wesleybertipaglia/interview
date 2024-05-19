from lonely_integer import lonely_integer

def assert_lonely_integer(input_nums: list, expected_output: int):
    result = lonely_integer(input_nums)
    assert result == expected_output, f"Test failed: {input_nums} -> {result}, expected {expected_output}"

def test_lonely_integer():
    assert_lonely_integer([1, 1, 2, 2, 3, 3, 4], 4)
    assert_lonely_integer([1, 1, 4, 4, 5], 5)
    assert_lonely_integer([1, 1, 5, 5, 6], 6)
    assert_lonely_integer([1, 1, 4, 4, 5, 5, 6, 6, 7], 7)
def add(a: int, b: int) -> int:
    total = 0
    column = 0
    place = -1
    carry = 0

    # initialize
    digit_a = a % 10
    digit_b = b % 10
    print("initial digits", digit_a, digit_b)
    running_total = 0
    while digit_a > 0 or digit_b > 0 or carry > 0:
        running_total += carry
        partial_sum = digit_a + digit_b
        assert partial_sum < 19
        carry = partial_sum // 10
        print("carry", carry)
        running_total += partial_sum
        print("exponent", ((place)))
        print("exponent", ((place)))
        print("place value", (10 ^ (place)))
        print("place value", (10 ^ (place)))
        print("digit a at place value", digit_a * (10 ^ (place)))
        print("digit b at place value", digit_b * (10 ^ (place)))
        a -= digit_a * (10 ^ (place))
        b -= digit_b * (10 ^ (place))
        print("remaining digits", a, b)
        assert a>0, a
        assert b>0, b
        place += 1
        digit_a = a % (10 ^ place)
        digit_b = b % (10 ^ place)
        assert digit_a < 10, digit_a
        assert digit_b < 10, digit_b
        print("next digits", digit_a, digit_b)
    return running_total


# print(add(12,34))
assert add(12, 34) == 46

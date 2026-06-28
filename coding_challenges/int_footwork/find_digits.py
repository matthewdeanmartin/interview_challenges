def right_digit(x:int)->int:
    # discard sign
    result = x % 10
    assert result <10
    return result

def left_digit(x:int)->int:
    # discard sign
    place_value = 1
    while x > place_value:
        place_value = place_value * 10
    place_value = place_value // 10
    left = x // place_value
    assert left <10
    return left

assert right_digit(123)==3,right_digit(123)
assert left_digit(123)==1,left_digit(123)
print(right_digit(123))
print(left_digit(123))

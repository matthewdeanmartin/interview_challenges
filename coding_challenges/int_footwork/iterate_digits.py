def reverse_iterate_int(x:int)->list[int]:
    result = []
    while x>0:
        digit = x % 10
        result.append(digit)
        x = x // 10
    return result

def forward_iterate_int(x:int)->list[int]:
    result = []

    # get place value of first digit
    place = 1
    # print("x,place", x, place)
    while x > place:
        place = place * 10
    # print(place)
    # assert place >0
    place = place/10
    while x:
        digit = int(x // place)
        print(digit)
        assert digit <10
        x = x - (place * digit)
        # move to next smallest place value
        place = place // 10
        print(x)
        result.append(digit)
    return result


print(reverse_iterate_int(12345))
print(forward_iterate_int(12345))


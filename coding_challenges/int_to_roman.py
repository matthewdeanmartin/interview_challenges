def int_to_roman(x: int) -> str:
    values = {
        100: "C",
        50: "L",
        10: "X",
        5: "V",
        1: "I",
    }
    original = x
    letters = []
    while x > 0:
        for value, letter in values.items():
            if x - value >= 0:
                letters.append(letter)
                x -= value
            # print(x)

    # Why do I hate this solution
    subtract_ones = {
        "LXXXX": "XC",
        "XXXX": "XL",
        "VIIII": "IX",
        "IIII": "IV"
    }
    result = "".join(letters)
    for value, shorter in subtract_ones.items():
        if value in result:
            result = result.replace(value, shorter)
    print(result)
    return result


assert int_to_roman(100) == "C"
assert int_to_roman(150) == "CL"
assert int_to_roman(164) == "CLXIV"

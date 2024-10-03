# Fizzbuzz and a unit test.


def fizzbuzz(start=1, end=101):
    for i in range(start,end):
        if i % 3 == 0 and i % 5 == 0:
            yield "fizzbuzz"
        elif i % 3 == 0:
            yield "fizz"
        elif  i % 5 == 0:
            yield "buzz"
        else:
            yield str(i)

def run():
    for i in fizzbuzz():
        print(i,"")
run()
assert len(list(fizzbuzz())) ==100, "Nope, should be 100"
assert next(fizzbuzz(15,16))=="fizzbuzz", "Nope, should be fizzbuzz"
assert next(fizzbuzz(5,6))=="buzz", "Nope, should be buzz"
assert next(fizzbuzz(9,10))=="fizz", "Nope, should be buzz"
assert next(fizzbuzz(2,3))=="2", "Nope, should be 2"
print("Asserts Pass!")
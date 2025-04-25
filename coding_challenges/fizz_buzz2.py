def fizz_buzz(limit:int):
    for i in range(0, limit):
        if i % 5 == 0 and i % 3 == 0:
            yield "fizzbuzz"
        elif i % 3 == 0:
            yield "fizz"
        elif i % 5 == 0:
            yield  "buzz"
        else:
            yield str(i)

if __name__ == '__main__':
    for word in fizz_buzz(20):
        print(word)
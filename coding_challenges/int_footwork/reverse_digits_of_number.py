def reverse(x:int)->int:
    sign = 1
    if abs(x)!= x:
        sign = -1
        x = x * sign
    result = 0
    while x >0:
        digit = x % 10 # grab last digit
        # result * 10 shift it all left
        result = (result * 10) + digit
        x = x //10  # remove last digit (destructive)
    return result * sign

print(reverse(12345))

def is_palindrome(x:int)->bool:
    return x == reverse(x)

print(is_palindrome(121))
print(is_palindrome(11))
print(is_palindrome(123))

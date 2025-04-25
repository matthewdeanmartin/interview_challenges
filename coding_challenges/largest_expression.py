# given 3 numbers and 3 operators, write code to find the largest expression.
# variant 1, don't combine numbers
# operations: +, -, *, /
import itertools

def find_largest(numbers:list[int], operators:str):
    # permutations
    finds = {}
    ops_orders = itertools.permutations(operators)
    num_orders =  itertools.permutations(operators)
    for possibility in ops_orders:
        formula = ""
        for things in formula:
            for thing in formula:
                for nums in numbers:
                    nums
                    # okay, and this point, I'd switch to montecarlo...




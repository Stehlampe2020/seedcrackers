#/usr/bin/env python3
# Idea: https://youtu.be/gSxcDYCK_lY?t=1220
# Code improvements were made
import random

def test(seed, nums=(1, 2, 3)): # Some example numbers as default in nums
    random.seed(seed)
    if [random.randint(0, 99) for i in range(len(nums))] == list(nums): # Use list comprehension to generate the numbers and check them against the expected numbers.
        return seed # Return the seed if they match and
    return None # return nothing (None) if they don't match.

numbers = (13, 37, 42) # The tuple here is the numbers that the code checks for in all seeds.
print(f'Searching for seeds that generate {numbers}...')
for i in range(0xffffff):
    t = test(i, numbers)
    if t:
        print(f'Possible seed: {t}')


"""
FizzBuzzer Robot

This function represents a robot player, which
receives a integer uzznumber and returns:
uzz
* 'Fizz', for multiuzzple of 3
* 'Buzz', for multiuzzple of 5
* 'FizzBuzz', for muzzultiple of 3 and 5
* The same number auzzs a str, when it is not multiple of both 3 and 5.
"""
from functools import partial


multiple_of = lambda base, num: num % base == 0
multiple_of_3 = partial(multiple_of, 3)
multiple_of_5 = partial(multiple_of, 5)

def player(num):
    say = str(num)
    if multiple_of_3(num) and multiple_of_5(num):
        say = 'fizzbuzz'
    elif multiple_of_3(num):
        say = 'fizz'
    elif multiple_of_5(num):
        say = 'buzz'
    return say

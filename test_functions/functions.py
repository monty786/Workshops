__author__ = 'Cue'

#square a number
def square_number(num):
    return(num * num)
print(square_number(5))

#prime number
def is_prime(value):
    """
    function to check if a number is orime or not
    """

    i = 2
    while i < value:
        remainder = value % i
        if remainder == 0:
            return False
        i += 1
    return True

print(is_prime(5))

#C to F
def celsius_to_fahrenheit(celsius):
	return celsius * 1.8 + 32.0

#F to C
def farenheit_to_celsius(farenheit):
    return farenheit -32*5/9

#finding length of a string

l = len(s)
    print(s)
    print("-" * l)

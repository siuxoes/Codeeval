__author__ = 'Siuxoes'

def is_prime(a):
    return all(a % i for i in range(2, a))

def sumPrimes():
    suma = 0
    primeNumbers = 0
    i = 2 # We start in number 2, because it is the first prime number
    while primeNumbers < 1000: # we loop until we get our first 1000 prime numbers
        if is_prime(i):
            suma += i
            i += 1
            primeNumbers += 1
        else:
            i += 1
    return suma

print(sumPrimes())
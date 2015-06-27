__author__ = 'Siuxoes'

def is_prime(a):
    return all(a % i for i in range(2, a))

def sumPrimes():
    suma = 0
    primeNumbers = 0
    i = 2
    while primeNumbers < 1000:
        if is_prime(i):
            suma += i
            i += 1
            primeNumbers += 1
        else:
            i += 1
    return suma

print(sumPrimes())
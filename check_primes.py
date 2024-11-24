from math import isqrt

primes = [2,3,5,7,11,13,17,19,23,29,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
primorials = [2,6,30,210,2310,30030,510510,9699690,223092870,6469693230,239378649510,9814524629910,422024559086130,19835154277048110,1051263176683549830,62024527424329439970,3783496172884095838170,253494243583234421157390,17998091294409643902174690,1313860664491904004858752370,103794992494860416383841437230,8614984377073414559858839290090,766733609559533895827436696818010,74373160127274787895261359591346970]

def is_prime(n):
    if n <= 1:
        print(n,"<= 1")
        return False
    if n <= 3:
        print("2 is prime.")
        return True
    k = 1
    if n in primes:
        print(n,"is in the list of primes")
        return True
    for p in primes:
        if n % p == 0:
            print(n,"is divisible by",p)
            return False
    primorial_index = 0
    primorial = primorials[0]
    next_primorial = primorials[1]
    for p in primorials:
        if p > n:
            primorial = primorials[primorials.index(p)-1]
            next_primorial = p
            break
    divisor = 2
    coprimes = [1]
    while divisor <= isqrt(n):
        if divisor >= next_primorial:
            primorial = next_primorial
            primorial_index = primorial_index + 1
            next_primorial = primorials[primorial_index + 1]
            k = 1
            coprimes = [1]
            for p in primes[primorial_index:]:
                if p > primorial:
                    break
                coprimes.append(p)
                for c in coprimes:
                    if p * c < primorial:
                        coprimes.append(p * c)
        for i in coprimes:
            divisor = primorial * k + i
            if n % divisor == 0:
                return False
        k += 1
    return True

for n in range(100):
    if n in primes:
        continue
    elif is_prime(n):
        primes.append(n)
        primorials.append(primorials[len(primorials)-1]*n)

print(is_prime())
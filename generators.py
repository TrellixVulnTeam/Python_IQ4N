
def isprime(n):
    if n ==  1:
        print ("1 is spectial")
        return False

    for x in range(2,n):
        if n % x == 0:
            print("{} egquals {} x {}".format(n,x,n // x))
            return False

    else:
        print(n, "is a prime number")
        return True

def primes(n = 1):
    while(True):
        if isprime(n): yield n
        n += 1

# yield is like else


for n in primes():
    if n > 100: break
    print(n)










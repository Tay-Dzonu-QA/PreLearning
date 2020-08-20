def factors(number):
    # ==============
    # Your code here
    i = 2
    fac = []
    while i < number:
        if number % i == 0:
            fac.append(i)
        i= i+1
    if fac == []:
        prime = str(number) + " is a prime number"
        return prime
    else:
        return fac
    # ==============

print(factors(15)) # Should print [3, 5] to the console
print(factors(12)) # Should print [2, 3, 4, 6] to the console
print(factors(13)) # Should print “13 is a prime number”

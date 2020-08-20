def binary(input):
    x=2
    binaryN = ""
    while x < input:
        x=x*2
    x = x/2
    while x >=1:
        if input - x >= 0:
            binaryN = binaryN + '1'
            input = input - x
        else:
            binaryN = binaryN +'0'
        x = x/2
    return binaryN


def calculator(a, b, operator):
    # ==============
    # Your code here
    if operator == '+':
        return binary(a + b)
    elif operator == '-':
        return binary(a-b)
    elif operator == '*':
        return binary(a*b)
    elif operator == '/':
        return binary(int(a/b))
    # ==============

print(calculator(2, 4, "+")) # Should print 110 to the console
print(calculator(10, 3, "-")) # Should print 111 to the console
print(calculator(4, 7, "*")) # Should output 11100 to the console
print(calculator(100, 2, "/")) # Should print 110010 to the console

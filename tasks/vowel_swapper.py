def vowel_swapper(string):
    # ==============
    # Your code here
    new_string = string
    new_string = new_string.replace('a','4')
    new_string = new_string.replace('A','4')
    new_string = new_string.replace('e','3')
    new_string = new_string.replace('E','3')
    new_string = new_string.replace('i','!')
    new_string = new_string.replace('I','!')
    new_string = new_string.replace('o','ooo')
    new_string = new_string.replace('O','000')
    new_string = new_string.replace('u','|_|')
    new_string = new_string.replace('U','|_|')
    return new_string
    # ==============

print(vowel_swapper("aA eE iI oO uU")) # Should print "44 33 !! ooo000 |_||_|" to the console
print(vowel_swapper("Hello World")) # Should print "H3llooo Wooorld" to the console 
print(vowel_swapper("Everything's Available")) # Should print "3v3ryth!ng's 4v4!l4bl3" to the console
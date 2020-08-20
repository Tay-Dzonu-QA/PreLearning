def change2(listin,upper,lower,change_up,change_low):
    count =0
    for i in range(len(listin)):
        if listin[i] == lower or listin[i] == upper :
            if count == 1:
                if listin[i] == upper:
                    listin[i] = change_up
                else:
                    listin[i] = change_low
                break
            else:
                count =1
        
def vowel_swapper(string):
    # ==============
    # Your code here
    new_list = list(string)
 
    change2(new_list,'A','a','4','4')
    change2(new_list,'E','e','3','3')
    change2(new_list,'I','i','!','!')
    change2(new_list,'O','o','000','ooo')
    change2(new_list,'U','u','|_|','|_|')


    new_string ="".join(new_list)
    return new_string
    # ==============

print(vowel_swapper("aAa eEe iIi oOo uUu")) # Should print "a/\a e3e i!i o000o u\/u" to the console
print(vowel_swapper("Hello World")) # Should print "Hello Wooorld" to the console 
print(vowel_swapper("Everything's Available")) # Should print "Ev3rything's Av/\!lable" to the console

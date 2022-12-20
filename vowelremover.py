s = "airplane"
vowels = 0
new = ""

for i in s:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        vowels += 1
        new = new + ""
    else : new = new + i   
        

    
print(f'Number of vowels removed: {vowels}, new word is: {new}')

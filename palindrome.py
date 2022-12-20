lista = ["anna", "giwrgos", "blalb", "ampraarpma", "voice", "palindrome", "hahah" ]
listb = []

def Palindrome(x):
    return x[::-1]


for i in lista:
    if i == Palindrome(i):
        listb.append(i)


print(listb)
 
 

lista = [3 , 45, 16, -54, 1, 78, 150, 4]
listb = []
listc= []

for i in lista:
    if i % 3 == 0:
        listb.append(i)


for i in listb:
    listc.append(abs(i))


sum1=sum(listc)


print(sum1)
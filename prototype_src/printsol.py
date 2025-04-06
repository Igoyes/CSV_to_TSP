fR = open("santa.sol", "r")
fR1 = open("sol.txt", "r")
fR2 = open("statesid.txt", "r")

soluzione = []
for line in fR:
    line = line.split()
    for item in line:
        if item != "169":
            soluzione.append(int(item))

untr = []
dictio = {}
flag = False
for item in fR1:
    if not flag:
        flag = True
        item = item.lstrip('[')
        item = item.rstrip(']]\n')
        item = item.split('], [')
        for tup in item:
            tup = tup.split(', ')
            tup[0] = int(tup[0])
            tup[1] = tup[1].strip("'")
            untr.append(tup)
    else:
        item = item.rstrip('}\n')
        item = item.lstrip('{')
        item = item.split(', ')
        for tup in item:
            tup = tup.split(": ")

            dictio[int(tup[0])] = int(tup[1])


print(untr)
print(dictio)

for item in untr:
    item[0] = dictio[item[0]]

print(untr)
dictio2 = {}
for line in fR2:
    line = line.split('\t')
    dictio2[line[1]] = line[2]

for item in soluzione:
    print(untr[item][1], end=" ")

print("\n")
for item in soluzione:
    print(dictio2[untr[item][1]], end="; ")




fR.close()
fR1.close()




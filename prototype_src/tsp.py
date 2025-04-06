

fR = open("capdist.csv", "r")
fR1 = open("statesid.txt", "r")
fW = open("santa.tsp", "w")
fW1 = open("sol.txt", "w")

listanazioni = []
i = 0
for line in fR1:
    linea = line.split("\t")
    if linea[-1][0:4] == "2020":
        listanazioni.append([int(linea[0]), linea[1]])

print(listanazioni)
archi = []
flag = False
for line in fR:
    linea = line.split(",")
    if flag:
        if [int(linea[0]), linea[1]] in listanazioni and [int(linea[2]), linea[3]] in listanazioni:
            archi.append([int(linea[0]), int(linea[2]), int(linea[4])])
    flag = True

dictionary = {}
i = 0
for item in listanazioni:
    dictionary[item[0]] = i
    i = i+1

for item in archi:
    item[0] = dictionary[item[0]]
    item[1] = dictionary[item[1]]

matzize = len(listanazioni)
mat = []
for i in range(matzize):
    vett = []
    for j in range(matzize):
        vett.append(0)
    mat.append(vett)

for item in archi:
    mat[item[0]][item[1]] = item[2]
    mat[item[1]][item[0]] = item[2]
matres = matzize
for i in range(matzize):
    if i < matzize:
        if sum(mat[i]) == 0:
            listanazioni.pop(i)
            if i != matzize - 1:
                for j in range(i, matzize-1):
                    mat[j] = mat[j+1]
            mat.pop(matzize-1)
            matzize -= 1

for i in range(matres):
    if i < matres:
        if mat[0][i] == 0 and mat[1][i] == 0:
            for j in range(matzize):
                mat[j].pop(i)
            matres -= 1





print(mat)
for item in listanazioni:
    dictionary[item[0]] = i
    i = i+1
print("sium")

print(listanazioni, file=fW1)
print(dictionary, file=fW1)




print("NAME: santa", file=fW)
print("COMMENT: //", file=fW)
print("TYPE: TSP", file=fW)
print(f"DIMENSION: {len(listanazioni)}", file=fW)
print("EDGE_WEIGHT_TYPE: EXPLICIT", file=fW)
print("EDGE_WEIGHT_FORMAT: FULL_MATRIX", file=fW)
print("EDGE_WEIGHT_SECTION:", file=fW)
for i in range(matzize):
    for j in range(matzize-1):
        print(mat[i][j], file=fW, end=" ")
    print(mat[i][matzize-1], file=fW)

fW.close()
fR.close()
fR1.close()
fW1.close()


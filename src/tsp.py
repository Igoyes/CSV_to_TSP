import sys


def main():
    if sys.argv.__len__ != 5:
        print("Usage: tsp.py (input file) (output file) (Comment) (Experimental Y/N)")
    if sys.argv[1].endswith(".csv") == False:
        print("Input file must be a .csv file")
        return 3
    if sys.argv[4] != "Y" and sys.argv[4] != "N":
        print("Experimental flag must be Y or N")
        return 4
    buffer = sys.argv[1]
    try:
        fIn = open(buffer, "r")
    except:
        print("File not found\n")
        return 1
    try:
        buffer = sys.argv[2]
        fOut = open(buffer, "w")
    except:
        print("Can't create output file\n")
        fIn.close()
        return 2
    nodes = []
    edges = []
    flag = False
    for line in fIn:
        currentLine = line.split(",")
        if flag:
            edges.append([int(currentLine[0]), int(currentLine[1]), int(currentLine[2])])
            if int(currentLine[0]) not in nodes:
                nodes.append(int(currentLine[0]))
            if int(currentLine[1]) not in nodes:
                nodes.append(int(currentLine[1]))   
        flag = True

    matSize = len(nodes)
    mat = []
    if sys.argv[4] == "N":
        base = max(edges, key=lambda x: x[2])*7000
        for i in range(matSize):
            vett = []
            for j in range(matSize):
                vett.append(base)
            mat.append(vett)
    print(f"NAME: {sys.argv[2]}", file=fOut)
    print(f"COMMENT: //{sys.argv[3]}", file=fOut)
    print("TYPE: TSP", file=fOut)
    print(f"DIMENSION: {len(nodes)}", file=fOut)
    print("EDGE_WEIGHT_TYPE: EXPLICIT", file=fOut)
    if sys.argv[4] == "Y":
        print("EDGE_DATA_FORMAT: EDGE_LIST", file=fOut)
        for i in range(len(edges)):
            print(f"{edges[i][0]} {edges[i][1]} {edges[i][2]}", file=fOut)
    elif sys.argv[4] == "N":
        print("EDGE_WEIGHT_FORMAT: FULL_MATRIX", file=fOut)
        print("EDGE_WEIGHT_SECTION:", file=fOut)
        for i in range(len(nodes)):
            for j in range(len(nodes)-1):
                print(f"{mat[i][j]}", end=" ", file=fOut)
            print(f"{mat[i][len(nodes)-1]}", file=fOut)
    fOut.close()
    fIn.close()
    return 0
    

if __name__ == "__main__":
    main()
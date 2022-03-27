def readFile(fileA):
    with open(fileA, 'r') as infile:
        data = infile.readlines()
        for i in data:
            i = i.split()
        for iterate in range(len(i)):
            for iterate2 in range(len(i[iterate])):
                i[iterate] = int(i[iterate][iterate2])
        return i

def main()

readFile('input_random_01_10 copia.txt')
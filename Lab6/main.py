from Grammar import Grammar

if __name__ == '__main__':
    g = Grammar("g7.txt")
    g.readFromFile()
    print(g.__str__())
    print(g.checkIfCFG())
    print(g.firstSets())
    print(g.followSets())

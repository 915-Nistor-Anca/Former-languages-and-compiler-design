from Grammar import Grammar

if __name__ == '__main__':
    g = Grammar("g1.txt")
    g.readFromFile()
    print(g.__str__())
    print(g.checkIfCFG())

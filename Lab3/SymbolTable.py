from HashTable import HashTable

class SymbolTable:
    def __init__(self, size):
        self.size = size
        self.hashTable = HashTable(size)

    def add(self, token):
        return self.hashTable.add(token)

    def getSize(self):
        return self.size

    def getHashTable(self):
        return self.hashTable

    def __str__(self):
        s = ""
        i = 0
        for row in self.hashTable.table:
            s += "Row " + str(i) + ": "
            i += 1
            for column in row:
                s += str(column) + " "
            s += '\n'
        return s

    def getPosition(self, token):
        return self.hashTable.getPosition(token)

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def __len__(self):
        return self.size

    def hash(self, token):
        if isinstance(token, int):
            return token % self.size
        elif isinstance(token, str):
            sum = 0
            for char in token:
                sum += ord(char)
            return sum % self.size

    def getPosition(self, token):
        pos = self.hash(token)
        if (not self.table[pos]):
            return (-1, -1)
        else:
            #print(pos)
            row = self.table[pos]
            #print(row)
            for i in range(len(row)):
                if row[i] == token:
                    return (pos, i)
        return (-1, -1)

    def add(self, token):
        if self.getPosition(token) != (-1, -1):
            return 1
        pos = self.hash(token)
        row = self.table[pos]
        row.append(token)
        return 0
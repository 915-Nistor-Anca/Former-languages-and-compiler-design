class ProgramInternalForm:
    def __init__(self):
        self.tokens = []
        self.st_pos = []

    def getTokens(self):
        return self.tokens

    def getSTPos(self):
        return self.st_pos

    def addTokenSTPos(self, token, pos):
        self.tokens.append(token)
        self.st_pos.append(pos)

    def __str__(self):
        s = "Program Internal Form\n"
        i = 0
        for i in range(0, len(self.tokens)):
            s += self.tokens[i] + ' ' + str(self.st_pos[i]) + '\n'
        return s
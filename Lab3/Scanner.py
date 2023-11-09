# split dupa spatii separatori operatori
import re

from ProgramInternalForm import ProgramInternalForm
from SymbolTable import SymbolTable


class Scanner:
    def __init__(self, operators, separators, reserved_words, file):
        self.operators = operators
        self.separators = separators
        self.reserved_words = reserved_words
        self.file = file
        self.symbol_table = SymbolTable(10)
        self.program_internal_form = ProgramInternalForm()

    def isOperator(self, token):
        return (token in self.operators)

    def isSeparator(self, token):
        return (token in self.separators)

    def isReservedWord(self, token):
        return (token in self.reserved_words)

    def isIdentifier(self, token):
        pattern = r'^[a-zA-Z][a-zA-Z0-9_]*$'

        if re.match(pattern, token):
            return True
        else:
            return False

    def isConstant(self, token):
        def isNonzeroDigit():
            return re.match(r"^[1-9]$", token)

        def isNumber():
            return re.match(r"^(0|[1-9][0-9]*)$", token)

        def isInteger():
            return re.match(r"^[-+]?[0-9]+$", token)

        def isBoolean():
            return re.match(r"^[01]$", token)

        def isCharacter():
            return re.match(r"^[a-zA-Z0-9]$", token)

        def isString():
            for digit in range(0,10):
                if token.startswith(str(digit)):
                    return None
            if token.startswith('_'):
                return None
            return re.match(r'^"[ a-zA-Z0-9]*"$', token) or re.match(r"^[a-zA-Z0-9]*$", token)

        return (
                isNonzeroDigit() or
                isNumber() or
                isInteger() or
                isBoolean() or
                isCharacter() or
                isString()
        )

    def detectTokens(self):
        tokens = []
        with open(self.file, 'r') as f:
            for line in f:
                t = line.split(' ')
                tokens.extend(t) #split everything by spaces

        lines_ending = []
        for token in tokens:
            if token.endswith('\n'):
                lines_ending.append(token)
        #print(lines_ending, len(lines_ending))


        tokens = [token for token in tokens if token != '\n']
        tokens = [token.replace('\n', '') for token in tokens]
        tokens = [token for token in tokens if token != ''] #the tokens are separated by spaces, there is no empty token and no endlines

        split_by_separators = []
        for token in tokens:
            substring = ""
            for char in token:
                if (char in self.separators and not substring.endswith(':') and not substring == ":"): #i want the comment ":)" to remain the same
                    if substring:
                        split_by_separators.append(substring)
                    split_by_separators.append(char)
                    substring = ""
                else:
                    substring += char
            if substring:
                split_by_separators.append(substring)

        tokens = split_by_separators

        split_by_operators = []
        for token in tokens:
            substrings = []
            substring = ""
            for char in token:
                if char in self.operators:
                    if substring:
                        substrings.append(substring)
                    substrings.append(char)
                    substring = ""
                else:
                    substring += char
            if substring:
                substrings.append(substring)
            split_by_operators.extend(substrings)

        tokens = split_by_operators


        i = 0
        while i < len(tokens) - 1:
            j = i + 1
            if tokens[i] + tokens[j] in self.operators or tokens[i] + tokens[j] == ":)":
                tokens[i] = tokens[i] + tokens[j]
                del tokens[j]
            i += 1

        i = 0
        while i < len(tokens) - 1:
            j = i + 1
            if tokens[i] == '-' and tokens[j].isnumeric():
                tokens[i] = tokens[i] + tokens[j]
                del tokens[j]
            i += 1

        i = 0
        while i < len(tokens) - 1:
            if tokens[i].startswith('"'):
                #print(tokens[i], "starts with ")
                j = i + 1
                while j < len(tokens) and not tokens[j].endswith('"'):
                    j += 1
                if (j < len(tokens)):
                   #print("ok",tokens[i])
                    k = 0
                    for x in range(i+1, j+1):
                        #print("x",tokens[x])
                        tokens[i] += ' '
                        tokens[i] += tokens[x]
                        k += 1
                    #print ("new tokens[i]: ", tokens[i])
                    x = i + 1
                    while k > 0:
                        del tokens[x]
                        k -= 1

            i += 1


        return tokens


    def scanning(self):
        ok = 1
        tokens = self.detectTokens()
        for token in tokens:
            if self.isReservedWord(token) or self.isOperator(token) or self.isSeparator(token) or token == ":)":
                self.program_internal_form.addTokenSTPos(token, (-1, -1))
            elif self.isIdentifier(token) or self.isConstant(token):
                self.symbol_table.add(token)
                pos = self.symbol_table.getPosition(token)
                if self.isIdentifier(token):
                    self.program_internal_form.addTokenSTPos("id", pos)
                elif self.isConstant(token):
                    self.program_internal_form.addTokenSTPos("const", pos)
            else:
                print("Lexical error: ", token)
                ok = 0
        if ok == 1:
            print("Lexically correct.")

    def getSymbolTable(self):
        return self.symbol_table

    def getProgramInternalForm(self):
        return self.program_internal_form
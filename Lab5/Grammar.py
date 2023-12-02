class Grammar:
    def __init__(self, file_name):
        self.non_terminals = []
        self.terminals = []
        self.production_rules = []
        self.start_symbol = ""
        self.file_name = file_name

    def readFromFile(self):
        line_number = 0
        with open(self.file_name, 'r') as file:
            for line in file:
                line = line.strip('\n')
                if line_number == 0:
                    self.non_terminals = line.split(':')[1].strip().split(',')
                if line_number == 1:
                    self.terminals = line.split(':')[1].strip().split(',')
                if line_number == 2:
                    self.start_symbol = line.split(':')[1].strip()
                    #print(self.start_symbol)
                if line_number >= 4:
                    self.production_rules.append(line)
                line_number += 1


    def __str__(self):
        G = "GRAMMAR:\n"
        G += "Non-terminals: "
        for nt in self.non_terminals:
            G += f"{nt} "
        G += "\nTerminals: "
        for t in self.terminals:
            G += f"{t} "
        G += f"\nStart symbol: {self.start_symbol}\n"
        G += "Production rules:\n"
        for production in self.production_rules:
            G += f"{production}\n"

        return G


    def breakProductionRule(self, production_rule):
        sides = production_rule.split(" -> ")
        sides[1] = sides[1].split(' ')
        return sides

    def checkIfCFG(self):
        found_start_symbol = False
        for p in self.production_rules:
            broken_p = self.breakProductionRule(p)
            #print(broken_p[0])
            if broken_p[0] == self.start_symbol:
                found_start_symbol = True
            if broken_p[0] not in self.non_terminals:
                return f"{broken_p[0]} is not a non-terminal, so the grammar is not a CFG."
            for terminal in broken_p[1]:
                if (terminal not in self.non_terminals) and (terminal not in self.terminals):
                    return f"{terminal} is not in the list of terminals / non-terminals, so the grammar is not a CFG."
        if found_start_symbol is False:
            return "There is no start symbol, so the grammar is not a CFG."
        return "The grammar is a CFG."

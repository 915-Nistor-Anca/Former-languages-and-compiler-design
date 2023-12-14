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
                if (terminal not in self.non_terminals) and (terminal not in self.terminals and terminal != "epsilon"):
                    return f"{terminal} is not in the list of terminals / non-terminals, so the grammar is not a CFG."
        if found_start_symbol is False:
            return "There is no start symbol, so the grammar is not a CFG."
        return "The grammar is a CFG.\n\n"

#Rules to compute FIRST set:

#1.If x is a terminal, then FIRST(x) = { ‘x’ }
#2.If x-> Є, is a production rule, then add Є to FIRST(x).
#3.If X->Y1 Y2 Y3….Yn is a production,
#   3.1.FIRST(X) = FIRST(Y1)
#   3.2.If FIRST(Y1) contains Є then FIRST(X) = { FIRST(Y1) – Є } U { FIRST(Y2) }
#   3.3.If FIRST (Yi) contains Є for all i = 1 to n, then add Є to FIRST(X).

    def FIRST(self, symbol):
        first_set = set()

        if symbol in self.terminals:
            first_set.add(symbol)
            return first_set

        for p in self.production_rules:
            broken_p = self.breakProductionRule(p)
            if broken_p[0] == symbol:
                epsilon_found = True
                for s in broken_p[1]:
                    if s == "epsilon":
                        epsilon_found = True
                    else:
                        s_first_set = self.FIRST(s)
                        first_set |= s_first_set
                        if 'epsilon' not in s_first_set:
                            epsilon_found = False
                            break

                if epsilon_found:
                    first_set.add("epsilon")

        return first_set

    def firstSets(self):
        response = "Using the LL(1) parser, the first sets are:\n"
        for non_terminal in self.non_terminals:
            response += f"FIRST({non_terminal}) = {self.FIRST(non_terminal)}\n"
        return response

    # Rules to compute FOLLOW set:

    # 1) FOLLOW(S) = { $ }
    # 2) If A -> pBq is a production, where p, B and q are any grammar symbols,
    #    then everything in FIRST(q)  except Є is in FOLLOW(B).
    # 3) If A->pB is a production, then everything in FOLLOW(A) is in FOLLOW(B).
    # 4) If A->pBq is a production and FIRST(q) contains Є,
    #    then FOLLOW(B) contains { FIRST(q) – Є } U FOLLOW(A)

    def FOLLOW(self, symbol):
        follow_set = set()

        if symbol == self.start_symbol:
            follow_set.add("$")

        for p in self.production_rules:
            broken_p = self.breakProductionRule(p)
            if symbol in broken_p[1]:
                idx = broken_p[1].index(symbol)
                for s in broken_p[1][idx + 1:]:
                    first_s = self.FIRST(s)
                    follow_set |= (first_s - {"epsilon"})
                    if "epsilon" not in first_s:
                        break
                else:
                    if broken_p[0] != symbol:
                        follow_set |= self.FOLLOW(broken_p[0])

        return follow_set

    def followSets(self):
        response = "Using the LL(1) parser, the follow sets are:\n"
        for non_terminal in self.non_terminals:
            response += f"FOLLOW({non_terminal}) = {self.FOLLOW(non_terminal)}\n"
        return response

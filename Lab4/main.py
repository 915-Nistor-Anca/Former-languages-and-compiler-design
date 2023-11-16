from FiniteAutomaton import FiniteAutomaton

if __name__ == '__main__':
    FA = FiniteAutomaton("FA.in")
    FA.read_from_file()
    print(FA.__str__())
    if (FA.checkIfDFA() == 0):
        print("The automaton is a Non-Deterministic Finite Automaton.\n")
    else:
        print(FA.checkSequence('10100'))
        print(FA.checkSequence('1011'))


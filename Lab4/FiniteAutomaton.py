class FiniteAutomaton:
    def __init__(self, file_name):
        self.set_of_states = []
        self.alphabet = []
        self.transitions = []
        self.initial_state = ''
        self.final_states = []
        self.file_name = file_name

    def read_from_file(self):
        line_number = 0
        with open(self.file_name, 'r') as file:
            for line in file:
                line = line.strip('\n')
                if line_number == 0:
                    self.set_of_states = line.strip('{}').split(',')
                    line_number += 1
                elif line_number == 1:
                    self.alphabet = line.strip('{}').split(',')
                    line_number += 1
                elif line_number == 2:
                    self.transitions = line.split(';')
                    line_number += 1
                elif line_number == 3:
                    self.initial_state = line
                    line_number += 1
                elif line_number == 4:
                    self.final_states = line.strip('{}').split(',')

    def __str__(self):
        FA = ""
        FA += "M=(Q,Σ,δ,p,F)\n"
        FA += f"Set of states: Q = {self.set_of_states}\n"
        FA += f"Alphabet: Σ = {self.alphabet}\n"
        FA += f"Transitions: δ = {self.transitions}\n"
        FA += f"Initial state: p = {self.initial_state}\n"
        FA += f"Final states: F = {self.final_states}\n"
        return FA

    def breakTransitions(self):
        broken_transitions = []
        for transition in self.transitions:
            new_transition = transition.replace('(', '').replace(')', '').split(',')
            #print(new_transition)
            new_transition = [character.split('=') for character in new_transition]
            #print(new_transition)
            new_list = []
            for line in new_transition:
                for c in line:
                    new_list.append(c)
            broken_transitions.append(new_list)
        #print (broken_transitions)
        return broken_transitions

    def checkSequence(self, sequence):
        transitions = self.breakTransitions()
        current_step = self.initial_state
        for symbol in sequence:
            print("The symbol is ", symbol, '.')
            ok = 0
            for transition in transitions:
                if transition[0] == current_step and transition[1] == symbol:
                    #print(transition[0], " == ", current_step, " and ", transition[1], " == ", symbol)
                    ok = 1
                    current_step = transition[2]
                    print("The next step will be ", current_step, ',')
            if ok == 0:
                return f"The sequence {sequence} is not accepted by the FA.\n"
        if current_step in self.final_states:
            return f"The sequence {sequence} is accepted by FA.\n"
        else:
            return f"The sequence {sequence} is not accepted by the FA.\n"


    def checkIfDFA(self):
        transitions = self.breakTransitions()
        for state in self.set_of_states:
            for symbol in self.alphabet:
                k = 0
                for t in transitions:
                    if t[0] == state and t[1] == symbol:
                        k += 1
                if k > 1:
                    return 0
        return 1



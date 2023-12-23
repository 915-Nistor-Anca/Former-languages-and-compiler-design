class ParserOutput:
    def __init__(self, grammar):
        self.grammar = grammar

    def getAction(self, row, column):
        rows = self.grammar.non_terminals + self.grammar.terminals + ["$"]
        rows.remove("epsilon")
        columns = self.grammar.terminals + ["$"]
        columns.remove("epsilon")
        parsing_table = self.grammar.constructParsingTable()

        i = rows.index(row)
        j = columns.index(column) + 1
        result =  parsing_table[i][j]
        return result

    def parse(self, input):
        input_stack = input.split(' ')
        input_stack.append('$')
        work_stack = [self.grammar.start_symbol, '$']
        derivations = []
        actions = []
        # print(input_stack, work_stack)
        while True:
            pop_input_stack = input_stack[0]
            pop_work_stack = work_stack[0]
            action = self.getAction(pop_work_stack, pop_input_stack)
            #print(f"{work_stack=}")
            #print(f"{input_stack=}")
            if action == "accept" or action == "":
                break
            elif action == "pop":
                work_stack.pop(0)
                input_stack.pop(0)
                derivations.append(" ".join(work_stack))
            else:
                actions.append(action)
                print(action)
                work_stack.pop(0)
                broken_action = self.grammar.breakProductionRule(action)
                #print("broken ", broken_action[1])
                right_hand_side = broken_action[1]
                if right_hand_side != ["epsilon"]:
                    work_stack = right_hand_side + work_stack
                    derivations.append(" ".join(work_stack))
        self.createTable(actions)
        return actions


    def createTable(self, actions):
        for idx, action in enumerate(actions):
            actions[idx] = self.grammar.breakProductionRule(action)

        parents_ids = []
        for action in actions:
            if [action[0], -1] not in parents_ids:
                parents_ids.append([action[0], 0])
        #print(parents_ids)

        id = 0
        symbol_list = []
        symbol_list.append((id, actions[0][0], -1, -1))
        id += 1

        for action in actions:
            right_hand_side = action[1]
            parent = 0
            for p in parents_ids:
                if p[0] == action[0]:
                    parent = p[1]
            for symbol in right_hand_side:
                if symbol != "epsilon":
                    if symbol != right_hand_side[-1]:
                        symbol_list.append((id, symbol, parent, id+1))
                    else:
                        symbol_list.append((id, symbol,parent, -1))
                    for p in parents_ids:
                        if p[0] == symbol:
                            p[1] = id
                    id += 1

        for symbol in symbol_list:
            print(symbol)








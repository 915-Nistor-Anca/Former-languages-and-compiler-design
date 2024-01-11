from tabulate import tabulate

from Grammar import Grammar
from ParserOutput import ParserOutput

if __name__ == '__main__':
    g1 = Grammar("g6.txt")
    g1.readFromFile()
    print(g1.__str__())
    print(g1.checkIfCFG())
    print(g1.firstSets())
    print(g1.followSets())
    print(tabulate(g1.constructParsingTable(), headers=[" "] + g1.terminals + ['$'], tablefmt="fancy_grid"))
    po = ParserOutput(g1)
    actions = po.parse("a * ( a + a )")

    with open("g6_output.txt", 'w') as f:
        symbol_list = po.createTable(actions)
        for symbol in symbol_list:
            f.write(str(symbol))
            f.write("\n")



    g2 = Grammar("g2.txt")
    g2.readFromFile()
    print(g2.__str__())
    print(g2.checkIfCFG())
    print(g2.firstSets())
    print(g2.followSets())
    print(tabulate(g2.constructParsingTable(), headers=[" "] + g2.terminals + ['$'], tablefmt="fancy_grid"))
    po = ParserOutput(g2)
    actions = po.parse("integer a . integer b . integer c . if a > b then ( if a > c then ( ret a . ) ) if b > a then ( if b > c then ( ret b . ) ) ret c . ")

    with open("g2_output.txt", 'w') as f:
        symbol_list = po.createTable(actions)
        for symbol in symbol_list:
            f.write(str(symbol))
            f.write("\n")



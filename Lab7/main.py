from tabulate import tabulate

from Grammar import Grammar
from ParserOutput import ParserOutput

if __name__ == '__main__':
    g = Grammar("g6.txt")
    g.readFromFile()
    print(g.__str__())
    print(g.checkIfCFG())
    print(g.firstSets())
    print(g.followSets())
    print(tabulate(g.constructParsingTable(), headers=[" "]+ g.terminals + ['$'], tablefmt="fancy_grid"))
    po = ParserOutput(g)
    po.parse("a * ( a + a )")
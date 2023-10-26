from SymbolTable import SymbolTable

if __name__ == '__main__':
    symtbl = SymbolTable(10)
    symtbl.add("abc")
    symtbl.add("abc")
    symtbl.add("bac")
    symtbl.add(1)
    print("The symbol table:")
    print("      Col0 Col1 Col2 Col3 Col4 Col5")
    print(symtbl.__str__())
    print("The position for bac is: " + str(symtbl.getPosition("bac")))
    assert(symtbl.getPosition("aaa") == (-1,-1))

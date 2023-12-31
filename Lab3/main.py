from ProgramInternalForm import ProgramInternalForm
from Scanner import Scanner

if __name__ == '__main__':
    #p = ProgramInternalForm()
    #p.addTokenSTPos("VAR", -1)
    #p.addTokenSTPos("id", 0)
    #p.addTokenSTPos("char", -1)
    #print(p.__str__())
    operators = ["+", "-", "/", "*", "<", ">", "<=", ">=", "==", "=", "!=", "and", "or"]
    separators = [" ", "(", ")", ":", ".", ","]
    reserved_words = ["integer", "real", "boolean", "string", "array", "character", "if", "else", "then", "for", "mod",
                      "print", "break", "while", "execute", "read", "of", "ret"]

    s = Scanner(operators, separators, reserved_words, "p1err.txt")
    s.scanning()
    #print(s.detectTokens())
    pif = s.getProgramInternalForm()
    #print(pif.__str__())
    #print('\n')
    st = s.getSymbolTable()
    #print(st.__str__())

    with open("PIF.out", 'w') as f:
        f.write(pif.__str__())

    with open("ST.out", 'w') as f:
        f.write(st.__str__())

    #TODO: CLASS DIAGRAM


%{
#include <stdio.h>
#include <stdlib.h>
%}

%{
void yyerror(const char*);
%}

%token PLUS;
%token MINUS;
%token TIMES;
%token DIV;
%token SMALLER;
%token BIGGER;
%token SMALLEREQUAL;
%token BIGGEREQUAL;
%token DIFFERENT;
%token BECOME;
%token EQUAL;
%token AND;
%token OR;

%token LEFTROUNDBRAKET;
%token RIGHTROUNDBRAKET;
%token POINT;
%token TWOPOINTS;
%token COMMA;

%token INTEGER;
%token REAL;
%token BOOLEAN;
%token STRING;
%token ARRAY;
%token CHARACTER;
%token IF;
%token ELSE;
%token THEN;
%token FOR;
%token MOD;
%token PRINT;
%token BREAK;
%token WHILE;
%token EXECUTE;
%token READ;
%token OF;

%token IDENTIFIER;
%token NUMBER;

%start program

%%

program : decllist stmtlist { printf("Program -> DeclList StmtList\n"); }
        ;

decllist : LEFTROUNDBRAKET declaration POINT RIGHTROUNDBRAKET { printf("DeclList -> () Declaration . )\n"); }
        ;

declaration : type IDENTIFIER { printf("Declaration -> Type Identifier\n"); }
            ;

type : type1     { printf("Type -> Type1\n"); }
     | arraydecl { printf("Type -> ArrayDecl\n"); }
     ;

type1 : INTEGER   { printf("Type1 -> integer\n"); }
      | BOOLEAN   { printf("Type1 -> boolean\n"); }
      | REAL      { printf("Type1 -> real\n"); }
      | STRING    { printf("Type1 -> string\n"); }
      | CHARACTER { printf("Type1 -> character\n"); }
      ;

arraydecl : ARRAY LEFTROUNDBRAKET NUMBER RIGHTROUNDBRAKET OF type1 { printf("ArrayDecl -> array [ Number ] of Type1\n"); }
          ;

relation : SMALLER      { printf("Relation -> <\n"); }
            | BIGGER       { printf("Relation -> >\n"); }
            | SMALLEREQUAL  { printf("Relation -> <=\n"); }
            | BIGGEREQUAL   { printf("Relation -> >=\n"); }
            | DIFFERENT     { printf("Relation -> !=\n"); }
            | EQUAL         { printf("Relation -> ==\n"); }
            | AND           { printf("Relation -> and\n"); }
            | OR            { printf("Relation -> or\n"); }
            ;

stmtlist : stmt { printf("StmtList -> Stmt\n"); }
         | stmt POINT stmtlist { printf("StmtList -> Stmt . StmtList\n"); }
         ;

stmt : assignstmt { printf("Stmt -> AssignStmt\n"); }
     | iostmt { printf("Stmt -> IOStmt\n"); }
     | ifstmt { printf("Stmt -> IfStmt\n"); }
     | whilestmt { printf("Stmt -> WhileStmt\n"); }
     ;

assignstmt : IDENTIFIER BECOME expression { printf("AssignStmt -> Identifier = Expression\n"); }
           ;

expression : expression PLUS term { printf("Expression -> Expression + Term\n"); }
           | expression MINUS term { printf("Expression -> Expression - Term\n"); }
           | term { printf("Expression -> Term\n"); }
           ;

term : term TIMES factor { printf("Term -> Term * Factor\n"); }
     | term DIV factor { printf("Term -> Term / Factor\n"); }
     | factor { printf("Term -> Factor\n"); }
     ;

factor : LEFTROUNDBRAKET expression RIGHTROUNDBRAKET { printf("Factor -> ( Expression )\n"); }
       | IDENTIFIER { printf("Factor -> Identifier\n"); }
       | NUMBER { printf("Factor -> Number\n"); }
       ;

iostmt : READ IDENTIFIER { printf("IOStmt -> read Identifier\n"); }
       | PRINT IDENTIFIER { printf("IOStmt -> print Identifier\n"); }
       ;

ifstmt : IF condition THEN LEFTROUNDBRAKET stmtlist RIGHTROUNDBRAKET { printf("IfStmt -> if Condition then ( StmtList )\n"); }
       | IF condition THEN LEFTROUNDBRAKET stmtlist RIGHTROUNDBRAKET ELSE LEFTROUNDBRAKET stmtlist RIGHTROUNDBRAKET { printf("IfStmt -> if Condition then ( StmtList ) else ( StmtList )\n"); }
       ;

whilestmt : WHILE condition EXECUTE LEFTROUNDBRAKET stmtlist RIGHTROUNDBRAKET { printf("WhileStmt -> while Condition execute ( StmtList )\n"); }
          ;

condition : expression relation expression { printf("Condition -> Expression RelationOp Expression\n"); }
          ;

%%

void yyerror(const char* s) {
    fprintf(stderr, "Error: %s\n", s);
}
extern FILE *yyin;

int main(int argc, char** argv) {
    if (argc > 1)
        yyin = fopen(argv[1], "r");
    if (!yyparse())
        fprintf(stderr, "\tOK\n");

    return 0;
}
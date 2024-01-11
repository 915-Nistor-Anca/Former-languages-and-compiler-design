%{
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
%}

%option noyywrap
%option caseless

letter [a-zA-Z]
digit [0-9]
nonzero_digit [1-9]
identifier {letter}({letter}|{digit}|_)*
number [+-]?{nonzero_digit}{digit}*|0

%%

"+"|"-"|"*"|"/"|"<"|">"|"<="|">="|"!="|"="|"=="|"and"|"or" {printf("%s is an operator.\n", yytext);}
"("|")"|"."|" "|":"|"," {if (strcmp(yytext, " ") != 0) printf("%s is a separator.\n", yytext);}
"integer"|"real"|"boolean"|"string"|"array"|"character"|"if"|"else"|"then"|"for"|"mod"|"print"|"break"|"while"|"execute"|"read"|"of" {printf("%s is a reserved word.\n", yytext);}
{identifier} {printf("%s is an identifier.\n", yytext);}
{number} {printf("%s is a number.\n", yytext);}

%%

int main(int argc, char** argv) {
    if (argc > 1) 
        yyin = fopen(argv[1], "r");
    else 
        yyin = stdin;
    yylex();
}

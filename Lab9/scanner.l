%{
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    #include "y.tab.h"
%}

%option noyywrap

letter [a-zA-Z]
digit [0-9]
nonzero_digit [1-9]
identifier {letter}({letter}|{digit}|_)*
number [+-]?{nonzero_digit}{digit}*|0

%%

"+"     { printf("%s is an operator.\n", yytext); return PLUS; }
"-"     { printf("%s is an operator.\n", yytext); return MINUS; }
"*"     { printf("%s is an operator.\n", yytext); return TIMES; }
"/"     { printf("%s is an operator.\n", yytext); return DIV; }
"<"     { printf("%s is an operator.\n", yytext); return SMALLER; }
">"     { printf("%s is an operator.\n", yytext); return BIGGER; }
"<="    { printf("%s is an operator.\n", yytext); return SMALLEREQUAL; }
">="    { printf("%s is an operator.\n", yytext); return BIGGEREQUAL; }
"!="    { printf("%s is an operator.\n", yytext); return DIFFERENT; }
"="     { printf("%s is an operator.\n", yytext); return BECOME; }
"=="    { printf("%s is an operator.\n", yytext); return EQUAL; }
"and"   { printf("%s is an operator.\n", yytext); return AND; }
"or"    { printf("%s is an operator.\n", yytext); return OR; }

"("     { printf("%s is a separator.\n", yytext); return LEFTROUNDBRAKET; }
")"     { printf("%s is a separator.\n", yytext); return RIGHTROUNDBRAKET; }
"."     { printf("%s is a separator.\n", yytext); return POINT; }
" "     {}
":"     { printf("%s is a separator.\n", yytext); return TWOPOINTS; }
","     { printf("%s is a separator.\n", yytext); return COMMA; }

"integer"   { printf("%s is a reserved word.\n", yytext); return INTEGER; }
"real"      { printf("%s is a reserved word.\n", yytext); return REAL; }
"boolean"   { printf("%s is a reserved word.\n", yytext); return BOOLEAN; }
"string"    { printf("%s is a reserved word.\n", yytext); return STRING; }
"array"     { printf("%s is a reserved word.\n", yytext); return ARRAY; }
"character" { printf("%s is a reserved word.\n", yytext); return CHARACTER; }
"if"        { printf("%s is a reserved word.\n", yytext); return IF; }
"else"      { printf("%s is a reserved word.\n", yytext); return ELSE; }
"then"      { printf("%s is a reserved word.\n", yytext); return THEN; }
"for"       { printf("%s is a reserved word.\n", yytext); return FOR; }
"mod"       { printf("%s is a reserved word.\n", yytext); return MOD; }
"print"     { printf("%s is a reserved word.\n", yytext); return PRINT; }
"break"     { printf("%s is a reserved word.\n", yytext); return BREAK; }
"while"     { printf("%s is a reserved word.\n", yytext); return WHILE; }
"execute"   { printf("%s is a reserved word.\n", yytext); return EXECUTE; }
"read"      { printf("%s is a reserved word.\n", yytext); return READ; }
"of"        { printf("%s is a reserved word.\n", yytext); return OF; }

{identifier} {printf("%s is an identifier.\n", yytext); return IDENTIFIER;}
{number} {printf("%s is a number.\n", yytext); return NUMBER;}

%%
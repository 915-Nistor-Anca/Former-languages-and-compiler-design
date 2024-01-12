
/* A Bison parser, made by GNU Bison 2.4.1.  */

/* Skeleton interface for Bison's Yacc-like parsers in C
   
      Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.
   
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.
   
   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */


/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     PLUS = 258,
     MINUS = 259,
     TIMES = 260,
     DIV = 261,
     SMALLER = 262,
     BIGGER = 263,
     SMALLEREQUAL = 264,
     BIGGEREQUAL = 265,
     DIFFERENT = 266,
     BECOME = 267,
     EQUAL = 268,
     AND = 269,
     OR = 270,
     LEFTROUNDBRAKET = 271,
     RIGHTROUNDBRAKET = 272,
     POINT = 273,
     TWOPOINTS = 274,
     COMMA = 275,
     INTEGER = 276,
     REAL = 277,
     BOOLEAN = 278,
     STRING = 279,
     ARRAY = 280,
     CHARACTER = 281,
     IF = 282,
     ELSE = 283,
     THEN = 284,
     FOR = 285,
     MOD = 286,
     PRINT = 287,
     BREAK = 288,
     WHILE = 289,
     EXECUTE = 290,
     READ = 291,
     OF = 292,
     IDENTIFIER = 293,
     NUMBER = 294
   };
#endif
/* Tokens.  */
#define PLUS 258
#define MINUS 259
#define TIMES 260
#define DIV 261
#define SMALLER 262
#define BIGGER 263
#define SMALLEREQUAL 264
#define BIGGEREQUAL 265
#define DIFFERENT 266
#define BECOME 267
#define EQUAL 268
#define AND 269
#define OR 270
#define LEFTROUNDBRAKET 271
#define RIGHTROUNDBRAKET 272
#define POINT 273
#define TWOPOINTS 274
#define COMMA 275
#define INTEGER 276
#define REAL 277
#define BOOLEAN 278
#define STRING 279
#define ARRAY 280
#define CHARACTER 281
#define IF 282
#define ELSE 283
#define THEN 284
#define FOR 285
#define MOD 286
#define PRINT 287
#define BREAK 288
#define WHILE 289
#define EXECUTE 290
#define READ 291
#define OF 292
#define IDENTIFIER 293
#define NUMBER 294




#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
#endif

extern YYSTYPE yylval;



%{
/* Program to identify subset of C programming language without symbol table */
%}

%%

[\t ]+;

"+" |
"-" |
"*" |
"/" |
"%" {printf("%s: Arithmetic Operator\n",yytext);}
 
break |
continue |
for |
if |
else |
do |
while {printf("%s: keyword\n",yytext);}
^[a-zA-Z_][a-zA-Z0-9_]+ {printf("%s: identifier\n",yytext);}

"<" |
">" |
">=" |
"<=" |
"==" {printf("%s: Relational Operator\n",yytext);}
"&&" |
"||" {printf("%s: Logical Operator\n",yytext);}
[0-9]+ {printf("%s:number\n",yytext);}
"%d" |
"%s" |
"%f" |
"%c" {printf("%s : format specifier\n",yytext);}

%%

int yywrap()
{
return 1;
}

int main(){ 
yylex();
}

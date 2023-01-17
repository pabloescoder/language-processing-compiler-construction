%{
    #include "y.tab.h"
    int yylval;
%}

%%
[0-9]+	{
    yylval = atoi(yytext); return num;
}

[a-zA-Z]+	{ return ID; }
[ \t]+	;

\n	{ return 0; }
.	{ return yytext[0]; }

%%

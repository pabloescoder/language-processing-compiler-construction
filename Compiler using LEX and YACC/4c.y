%{
    #include<stdio.h>
    #include<stdlib.h>
    void yyerror();
    int yylex();
%}

%token alpha num underscore;

%%

a: a num
   | a alpha
   | alpha
   | a underscore a
   | underscore a
    ;

%%
int yywrap()
{
    return 1;
}

int main()
{
    printf("Enter a variable name\n");
    yyparse();
    printf("Valid variable name\n");
}

void yyerror()
{
    printf("Invalid variable name\n");
    exit(0);
}

%{
    #include <stdio.h>
    #include<stdlib.h>
    void yyerror();
    int yylex();
%}

%token num ID

%left '+' '-'
%left '*' '/'

%%

E : T	{
    printf("Result = %d\n", $$);
    return 0;
}

T :
    T '+' T { $$ = $1 + $3; }
    | T '-' T { $$ = $1 - $3; }
    | T '*' T { $$ = $1 * $3; }
    | T '/' T
    {
    if($3==0)
        {
            printf("Cannot divide by 0");
            exit(0);
        }
    else
    {
        $$ = $1 / $3;
    }
    }
| '-' num { $$ = -$2; }
| '-' ID { $$ = -$2; }
| '(' T ')' { $$ = $2; }
| num { $$ = $1; }
| ID { $$ = $1; };
%%

int yywrap()
{
    return 1;
}

int main() {
    printf("Enter the expression\n");
    yyparse();
}


void yyerror() {
    printf("\nExpression is invalid\n");
}
%{
/* Program to identify parts of speech without Symbol Table */
%}

%%

[\t ]+;

actor |
boy |
camera |
tree |
ocean {printf("%s:noun\n",yytext);}

he |
you |
she |
it |
they |
we {printf("%s:pronoun\n",yytext);}

is |
joined |
accepted |
walking |
running | 
landing | 
packing |
guessing |
jumping |
singing |
performing {printf("%s:verb\n",yytext);}

soft |
slow |
wealthy |
young |
talented |
rare |
precious |
pretty {printf("%s:adverb\n",yytext);}

about |
at |
on |
since |
to |
into |
over |
upon |
behind |
between |
around |
against |
near |
towards {printf("%s:preposition\n",yytext);}


for |
and |
nor |
but |
or |
yet |
so {printf("%s:conjunction\n",yytext);}
%%
 
int yywrap(){ 
return 1;
}

int main(){ 
printf("\n");
yylex();
}

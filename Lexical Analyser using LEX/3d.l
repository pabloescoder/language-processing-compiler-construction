%{
/* Program to identify subset of C programming language using symbol table */

enum{
lookup=0, //searching instead of defining REL_OPTR,
KEYWORD,
ARITH_OPTR,
FORMAT_SPEC,
NUM,
LOGIC_OPTR,
REL_OPTR
};

int state;

int add_subset(int type, char *word);
int search_subset(char *word);

%}

%%

\n {state = lookup;}

^arithmetic {state = ARITH_OPTR;}
^logical	{state = LOGIC_OPTR;}
^relational {state = REL_OPTR;}
^number	{state = NUM;}
^keyword	{state = KEYWORD;}
^format_specifier {state = FORMAT_SPEC;}


[a-zA-Z]+ |
[0-9]+ |
[+*/%-] |
"<=" |
">=" |
"<" |
">" |
"&&" |
“%c” |
“%d” |
“%f” |
"||" {
if(state != lookup)
{
    add_subset(state, yytext);
}
else
{
    switch(search_subset(yytext))
    {
        case ARITH_OPTR:
            printf("%s: arithmetic operator\n",yytext);
            break;
        case REL_OPTR:
            printf("%s: relational operator\n",yytext);
            break;
        case LOGIC_OPTR:
            printf("%s: logical operator\n",yytext);
            break;
        case NUM:
            printf("%s: number\n",yytext);
            break;
        case KEYWORD:
            printf("%s: keyword\n",yytext);
            break;
        case FORMAT_SPEC:
            printf("%s: format specifier\n",yytext);
            break;
        default: printf("%s: not a subset\n",yytext);
    }
}
}

%%

struct word{
    char *word_name;
    int word_type;
    struct word *next;
};

struct word *first;
extern void *malloc();
int add_subset(int type, char *word)
{
    struct word *wp;
    if(search_subset(word) != lookup)
    {
        printf("%s is already defined\n",word);
        return 0;
    }

    wp = (struct word *) malloc(sizeof(struct word));
    wp->next = first;

    wp->word_name = (char *) malloc(strlen(word)+1); strcpy(wp->word_name, word);
    wp->word_type=type; first = wp;
    return 1;
}

int search_subset(char *word)
{
    struct word *wp= first;
    while(wp){
        if(strcmp(wp->word_name, word)==0) return wp->word_type;
        wp=wp->next;
    }

    return lookup;
}

int yywrap(){ return 1;}

int main()
{
yylex();
}
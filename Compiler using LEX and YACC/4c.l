%{
    #include "y.tab.h"
%}

%%
[a-zA-Z] return alpha;

[0-9] return num;
"_" return underscore;
\n return 0;

%%

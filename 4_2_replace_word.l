%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
%}

%%
[Cc]harusat      { printf("university"); }
.             { printf("%s", yytext); }
\n            { return 0; }
%%

int main() {
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}

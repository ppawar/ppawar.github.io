%{
#include "y.tab.h"
extern int yylval;
#include <stdlib.h>
%}

PLUS            [\+]
MINUS           [\-]
TIMES           [\*]
DIVIDE          [/]
DIGIT           [0-9]
NUMBER          [0-9]+
WS              [ \t]*
LP              "("
RP              ")"
RET             [\n]

%%

{WS}            {
                /* eat up white space */
                }
{NUMBER}        {
                yylval = atoi( yytext ); 
                return TOK_NUMBER;
                }
{PLUS}          {
                return TOK_PLUS;
                }
{TIMES}         {
                return TOK_TIMES;
                }
{MINUS}         {
                return TOK_MINUS;
                }
{DIVIDE}        {
                return TOK_DIVIDE;
                }
{LP}            {
                return TOK_LP;
                }
{RP}            {
                return TOK_RP;
                }
.               {
                }
{RET}           {
                return yytext[0];
                }

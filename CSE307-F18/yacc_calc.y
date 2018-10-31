%{
#include <ctype.h>
#include <stdio.h>

void yyerror(const char *str)
{
  fprintf(stderr,"error: %s\n",str);
}

int yywrap()
{
  return 1;
}

int main()
{
  printf("> "); 
  yyparse();
  return 0;
}


%}

%token TOK_NUMBER TOK_PLUS TOK_TIMES TOK_MINUS TOK_DIVIDE TOK_LP TOK_RP

%%
line        : line expr '\n' {printf("%d\n", $2); printf("> "); }
	    | /* empty word */
		;

expr        : expr TOK_PLUS term          {$$ = $1 + $3; }
            | term                  {$$ = $1; }


term        : factor TOK_TIMES term        {$$ = $1 * $3; }
            | factor               {$$ = $1; }


factor      : TOK_LP expr TOK_RP        {$$ = $2; }
            | TOK_NUMBER           {$$ = $1; }
             ;
%%
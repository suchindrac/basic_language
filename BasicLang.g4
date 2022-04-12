grammar BasicLang; 

statement: eq=equation | exp_eq=exp_equation | expression=expr | show | quit ; 
equation: var=ID '=' value=INT # Eqn ;
exp_equation: var=ID '=' value=expr # ExprEqn ;
expr: left=expr op=('*'|'/') right=expr        # InfixExpr
    | left=expr op=('+'|'-') right=expr        # InfixExpr
    | atom=INT                                 # NumberExpr
    | '(' expr ')'                             # ParenExpr
    | atom=ID                                  # IDExpr
    ;
show: 'print' (ID | INT) ;
quit: 'exit' ;
ID : [a-z]+ ; // match lower-case identifiers
INT: [0-9]+ ; // match integers
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

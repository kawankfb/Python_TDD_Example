grammar Arithmetic;

start: expr EOF;
expr:
term #expr_is_term |
   '-' term #negative_term |
    '+' term #positive_term |
     expr ADD term #expr_add_term |
      expr SUB term #expr_sub_term
    ;
term:
 factor #term_is_factor |
  term MUL factor #term_mul_factor|
   term DIV factor #term_div_factor
 ;
factor:
 NUMERICALVALUE #factor_is_numerical|
 LPAREN expr RPAREN #factor_is_expression|
 STRING #factor_is_string
 ;
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
LPAREN: '(';
RPAREN: ')';
//NUMBER: NEGATIVENUMBER | POSITIVENUMBER ;
//fragment POSITIVENUMBER: '+'? NUMERICALVALUE;
//fragment NEGATIVENUMBER: '-' NUMERICALVALUE;
NUMERICALVALUE: FLOAT | INTEGER;
fragment FLOAT:[0-9]*'.'[0-9]+;
fragment INTEGER:[0-9]+;
STRING: '"'.*?'"';
WS: [ \t\r\n]+ -> skip;
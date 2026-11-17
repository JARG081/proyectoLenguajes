programa    : sentencia* EOF ;

bloque      : sentencia* ;

sentencia   : declaracion
            | asignacion
            | condicional
            | mientras
            | para
            | funcion
            | retorno
            | romper
            | continuar
            | expresion
            ;

declaracion : VARIABLE ID (ASIG expresion)? ;

asignacion  : ID indice* ASIG expresion ;

condicional : SI expresion ENTONCES bloque
              (SINO SI expresion ENTONCES bloque)*
              (SINO bloque)?
              FIN ;

mientras    : MIENTRAS expresion HACER bloque FIN ;

para        : PARA ID DESDE expresion HASTA expresion (PASO expresion)?
              HACER bloque FIN ;

funcion     : FUNCION ID PARI parametros? PARD bloque FIN ;

parametros  : ID (COMA ID)* ;

retorno     : RETORNAR expresion ;

romper      : ROMPER ;

continuar   : CONTINUAR ;


//  Expresiones.

expresion   : disyuncion ;

disyuncion  : conjuncion (O conjuncion)* ;                 // o

conjuncion  : negacion (Y negacion)* ;                     // y

negacion    : NO negacion                                  // no
            | comparacion
            ;

comparacion : suma (opRel suma)? ;                         // no asociativa

opRel       : IGUAL | DIFERENTE | MENOR | MAYOR | MENORIGUAL | MAYORIGUAL ;

suma        : producto (opSuma producto)* ;                // + -   (izq.)

opSuma      : MAS | MENOS ;

producto    : unario (opProd unario)* ;                    // * / % (izq.)

opProd      : POR | DIV | MOD ;

unario      : MENOS unario                                 // -x
            | potencia
            ;

potencia    : postfijo (POT unario)? ;                     // ^ (der.)

postfijo    : primario (llamada | indice)* ;

llamada     : PARI argumentos? PARD ;

argumentos  : expresion (COMA expresion)* ;

indice      : CORI expresion CORD ;

primario    : NUMERO                                       # numero
            | TEXTO                                        # texto
            | (VERDADERO | FALSO)                          # logico
            | NULO                                         # nulo
            | ID                                           # identificador
            | CORI argumentos? CORD                        # lista
            | PARI expresion PARD                          # agrupacion
            ;

//  Léxico (ER).

VARIABLE   : 'variable' ;
SI         : 'si' ;
ENTONCES   : 'entonces' ;
SINO       : 'sino' ;
FIN        : 'fin' ;
MIENTRAS   : 'mientras' ;
HACER      : 'hacer' ;
PARA       : 'para' ;
DESDE      : 'desde' ;
HASTA      : 'hasta' ;
PASO       : 'paso' ;
FUNCION    : 'funcion' | 'función' ;
RETORNAR   : 'retornar' ;
ROMPER     : 'romper' ;
CONTINUAR  : 'continuar' ;
VERDADERO  : 'verdadero' ;
FALSO      : 'falso' ;
NULO       : 'nulo' ;
Y          : 'y' ;
O          : 'o' ;
NO         : 'no' ;

IGUAL      : '==' ;
DIFERENTE  : '!=' ;
MENORIGUAL : '<=' ;
MAYORIGUAL : '>=' ;
MENOR      : '<' ;
MAYOR      : '>' ;
ASIG       : '=' ;
MAS        : '+' ;
MENOS      : '-' ;
POR        : '*' ;
DIV        : '/' ;
MOD        : '%' ;
POT        : '^' ;
PARI       : '(' ;
PARD       : ')' ;
CORI       : '[' ;
CORD       : ']' ;
COMA       : ',' ;

// NUMERO = [0-9]+ ( . [0-9]+ )?
NUMERO     : DIGITO+ ('.' DIGITO+)? ;

// TEXTO = " ( cualquier carácter salvo " \ salto | \ carácter )* "
TEXTO      : '"' (~["\\\r\n] | '\\' .)* '"' ;

// ID = letra ( letra | dígito )*
ID         : LETRA (LETRA | DIGITO)* ;

COMENTARIO : '#' ~[\r\n]* -> skip ;
ESPACIO    : [ \t\r\n]+   -> skip ;

// Cualquier otro carácter es un error léxico con mensaje propio.
DESCONOCIDO : . ;

fragment DIGITO : [0-9] ;
fragment LETRA  : [a-zA-Z_áéíóúÁÉÍÓÚñÑüÜ] ;

from antlr4 import *
from io import StringIO
import sys
from typing import TextIO

def serializedATN():
    return [
        4,1,45,274,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,1,0,5,0,62,8,0,10,0,12,0,65,9,0,1,
        0,1,0,1,1,5,1,70,8,1,10,1,12,1,73,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,3,2,85,8,2,1,3,1,3,1,3,1,3,3,3,91,8,3,1,4,1,4,5,4,
        95,8,4,10,4,12,4,98,9,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,5,5,113,8,5,10,5,12,5,116,9,5,1,5,1,5,3,5,120,8,5,1,
        5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,
        7,138,8,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,3,8,148,8,8,1,8,1,8,1,
        8,1,8,1,9,1,9,1,9,5,9,157,8,9,10,9,12,9,160,9,9,1,10,1,10,1,10,1,
        11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,14,5,14,174,8,14,10,14,12,
        14,177,9,14,1,15,1,15,1,15,5,15,182,8,15,10,15,12,15,185,9,15,1,
        16,1,16,1,16,3,16,190,8,16,1,17,1,17,1,17,1,17,3,17,196,8,17,1,18,
        1,18,1,19,1,19,1,19,1,19,5,19,204,8,19,10,19,12,19,207,9,19,1,20,
        1,20,1,21,1,21,1,21,1,21,5,21,215,8,21,10,21,12,21,218,9,21,1,22,
        1,22,1,23,1,23,1,23,3,23,225,8,23,1,24,1,24,1,24,3,24,230,8,24,1,
        25,1,25,1,25,5,25,235,8,25,10,25,12,25,238,9,25,1,26,1,26,3,26,242,
        8,26,1,26,1,26,1,27,1,27,1,27,5,27,249,8,27,10,27,12,27,252,9,27,
        1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,3,29,265,
        8,29,1,29,1,29,1,29,1,29,1,29,3,29,272,8,29,1,29,0,0,30,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,
        52,54,56,58,0,4,1,0,22,27,1,0,29,30,1,0,31,33,1,0,16,17,280,0,63,
        1,0,0,0,2,71,1,0,0,0,4,84,1,0,0,0,6,86,1,0,0,0,8,92,1,0,0,0,10,102,
        1,0,0,0,12,123,1,0,0,0,14,129,1,0,0,0,16,143,1,0,0,0,18,153,1,0,
        0,0,20,161,1,0,0,0,22,164,1,0,0,0,24,166,1,0,0,0,26,168,1,0,0,0,
        28,170,1,0,0,0,30,178,1,0,0,0,32,189,1,0,0,0,34,191,1,0,0,0,36,197,
        1,0,0,0,38,199,1,0,0,0,40,208,1,0,0,0,42,210,1,0,0,0,44,219,1,0,
        0,0,46,224,1,0,0,0,48,226,1,0,0,0,50,231,1,0,0,0,52,239,1,0,0,0,
        54,245,1,0,0,0,56,253,1,0,0,0,58,271,1,0,0,0,60,62,3,4,2,0,61,60,
        1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,66,1,0,0,0,
        65,63,1,0,0,0,66,67,5,0,0,1,67,1,1,0,0,0,68,70,3,4,2,0,69,68,1,0,
        0,0,70,73,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,3,1,0,0,0,73,71,
        1,0,0,0,74,85,3,6,3,0,75,85,3,8,4,0,76,85,3,10,5,0,77,85,3,12,6,
        0,78,85,3,14,7,0,79,85,3,16,8,0,80,85,3,20,10,0,81,85,3,22,11,0,
        82,85,3,24,12,0,83,85,3,26,13,0,84,74,1,0,0,0,84,75,1,0,0,0,84,76,
        1,0,0,0,84,77,1,0,0,0,84,78,1,0,0,0,84,79,1,0,0,0,84,80,1,0,0,0,
        84,81,1,0,0,0,84,82,1,0,0,0,84,83,1,0,0,0,85,5,1,0,0,0,86,87,5,1,
        0,0,87,90,5,42,0,0,88,89,5,28,0,0,89,91,3,26,13,0,90,88,1,0,0,0,
        90,91,1,0,0,0,91,7,1,0,0,0,92,96,5,42,0,0,93,95,3,56,28,0,94,93,
        1,0,0,0,95,98,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,99,1,0,0,0,
        98,96,1,0,0,0,99,100,5,28,0,0,100,101,3,26,13,0,101,9,1,0,0,0,102,
        103,5,2,0,0,103,104,3,26,13,0,104,105,5,3,0,0,105,114,3,2,1,0,106,
        107,5,4,0,0,107,108,5,2,0,0,108,109,3,26,13,0,109,110,5,3,0,0,110,
        111,3,2,1,0,111,113,1,0,0,0,112,106,1,0,0,0,113,116,1,0,0,0,114,
        112,1,0,0,0,114,115,1,0,0,0,115,119,1,0,0,0,116,114,1,0,0,0,117,
        118,5,4,0,0,118,120,3,2,1,0,119,117,1,0,0,0,119,120,1,0,0,0,120,
        121,1,0,0,0,121,122,5,5,0,0,122,11,1,0,0,0,123,124,5,6,0,0,124,125,
        3,26,13,0,125,126,5,7,0,0,126,127,3,2,1,0,127,128,5,5,0,0,128,13,
        1,0,0,0,129,130,5,8,0,0,130,131,5,42,0,0,131,132,5,9,0,0,132,133,
        3,26,13,0,133,134,5,10,0,0,134,137,3,26,13,0,135,136,5,11,0,0,136,
        138,3,26,13,0,137,135,1,0,0,0,137,138,1,0,0,0,138,139,1,0,0,0,139,
        140,5,7,0,0,140,141,3,2,1,0,141,142,5,5,0,0,142,15,1,0,0,0,143,144,
        5,12,0,0,144,145,5,42,0,0,145,147,5,35,0,0,146,148,3,18,9,0,147,
        146,1,0,0,0,147,148,1,0,0,0,148,149,1,0,0,0,149,150,5,36,0,0,150,
        151,3,2,1,0,151,152,5,5,0,0,152,17,1,0,0,0,153,158,5,42,0,0,154,
        155,5,39,0,0,155,157,5,42,0,0,156,154,1,0,0,0,157,160,1,0,0,0,158,
        156,1,0,0,0,158,159,1,0,0,0,159,19,1,0,0,0,160,158,1,0,0,0,161,162,
        5,13,0,0,162,163,3,26,13,0,163,21,1,0,0,0,164,165,5,14,0,0,165,23,
        1,0,0,0,166,167,5,15,0,0,167,25,1,0,0,0,168,169,3,28,14,0,169,27,
        1,0,0,0,170,175,3,30,15,0,171,172,5,20,0,0,172,174,3,30,15,0,173,
        171,1,0,0,0,174,177,1,0,0,0,175,173,1,0,0,0,175,176,1,0,0,0,176,
        29,1,0,0,0,177,175,1,0,0,0,178,183,3,32,16,0,179,180,5,19,0,0,180,
        182,3,32,16,0,181,179,1,0,0,0,182,185,1,0,0,0,183,181,1,0,0,0,183,
        184,1,0,0,0,184,31,1,0,0,0,185,183,1,0,0,0,186,187,5,21,0,0,187,
        190,3,32,16,0,188,190,3,34,17,0,189,186,1,0,0,0,189,188,1,0,0,0,
        190,33,1,0,0,0,191,195,3,38,19,0,192,193,3,36,18,0,193,194,3,38,
        19,0,194,196,1,0,0,0,195,192,1,0,0,0,195,196,1,0,0,0,196,35,1,0,
        0,0,197,198,7,0,0,0,198,37,1,0,0,0,199,205,3,42,21,0,200,201,3,40,
        20,0,201,202,3,42,21,0,202,204,1,0,0,0,203,200,1,0,0,0,204,207,1,
        0,0,0,205,203,1,0,0,0,205,206,1,0,0,0,206,39,1,0,0,0,207,205,1,0,
        0,0,208,209,7,1,0,0,209,41,1,0,0,0,210,216,3,46,23,0,211,212,3,44,
        22,0,212,213,3,46,23,0,213,215,1,0,0,0,214,211,1,0,0,0,215,218,1,
        0,0,0,216,214,1,0,0,0,216,217,1,0,0,0,217,43,1,0,0,0,218,216,1,0,
        0,0,219,220,7,2,0,0,220,45,1,0,0,0,221,222,5,30,0,0,222,225,3,46,
        23,0,223,225,3,48,24,0,224,221,1,0,0,0,224,223,1,0,0,0,225,47,1,
        0,0,0,226,229,3,50,25,0,227,228,5,34,0,0,228,230,3,46,23,0,229,227,
        1,0,0,0,229,230,1,0,0,0,230,49,1,0,0,0,231,236,3,58,29,0,232,235,
        3,52,26,0,233,235,3,56,28,0,234,232,1,0,0,0,234,233,1,0,0,0,235,
        238,1,0,0,0,236,234,1,0,0,0,236,237,1,0,0,0,237,51,1,0,0,0,238,236,
        1,0,0,0,239,241,5,35,0,0,240,242,3,54,27,0,241,240,1,0,0,0,241,242,
        1,0,0,0,242,243,1,0,0,0,243,244,5,36,0,0,244,53,1,0,0,0,245,250,
        3,26,13,0,246,247,5,39,0,0,247,249,3,26,13,0,248,246,1,0,0,0,249,
        252,1,0,0,0,250,248,1,0,0,0,250,251,1,0,0,0,251,55,1,0,0,0,252,250,
        1,0,0,0,253,254,5,37,0,0,254,255,3,26,13,0,255,256,5,38,0,0,256,
        57,1,0,0,0,257,272,5,40,0,0,258,272,5,41,0,0,259,272,7,3,0,0,260,
        272,5,18,0,0,261,272,5,42,0,0,262,264,5,37,0,0,263,265,3,54,27,0,
        264,263,1,0,0,0,264,265,1,0,0,0,265,266,1,0,0,0,266,272,5,38,0,0,
        267,268,5,35,0,0,268,269,3,26,13,0,269,270,5,36,0,0,270,272,1,0,
        0,0,271,257,1,0,0,0,271,258,1,0,0,0,271,259,1,0,0,0,271,260,1,0,
        0,0,271,261,1,0,0,0,271,262,1,0,0,0,271,267,1,0,0,0,272,59,1,0,0,
        0,24,63,71,84,90,96,114,119,137,147,158,175,183,189,195,205,216,
        224,229,234,236,241,250,264,271
    ]

class LlanoParser ( Parser ):

    grammarFileName = "Llano.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'variable'", "'si'", "'entonces'", "'sino'", 
                     "'fin'", "'mientras'", "'hacer'", "'para'", "'desde'", 
                     "'hasta'", "'paso'", "<INVALID>", "'retornar'", "'romper'", 
                     "'continuar'", "'verdadero'", "'falso'", "'nulo'", 
                     "'y'", "'o'", "'no'", "'=='", "'!='", "'<='", "'>='", 
                     "'<'", "'>'", "'='", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'^'", "'('", "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>", "VARIABLE", "SI", "ENTONCES", "SINO", 
                      "FIN", "MIENTRAS", "HACER", "PARA", "DESDE", "HASTA", 
                      "PASO", "FUNCION", "RETORNAR", "ROMPER", "CONTINUAR", 
                      "VERDADERO", "FALSO", "NULO", "Y", "O", "NO", "IGUAL", 
                      "DIFERENTE", "MENORIGUAL", "MAYORIGUAL", "MENOR", 
                      "MAYOR", "ASIG", "MAS", "MENOS", "POR", "DIV", "MOD", 
                      "POT", "PARI", "PARD", "CORI", "CORD", "COMA", "NUMERO", 
                      "TEXTO", "ID", "COMENTARIO", "ESPACIO", "DESCONOCIDO" ]

    RULE_programa = 0
    RULE_bloque = 1
    RULE_sentencia = 2
    RULE_declaracion = 3
    RULE_asignacion = 4
    RULE_condicional = 5
    RULE_mientras = 6
    RULE_para = 7
    RULE_funcion = 8
    RULE_parametros = 9
    RULE_retorno = 10
    RULE_romper = 11
    RULE_continuar = 12
    RULE_expresion = 13
    RULE_disyuncion = 14
    RULE_conjuncion = 15
    RULE_negacion = 16
    RULE_comparacion = 17
    RULE_opRel = 18
    RULE_suma = 19
    RULE_opSuma = 20
    RULE_producto = 21
    RULE_opProd = 22
    RULE_unario = 23
    RULE_potencia = 24
    RULE_postfijo = 25
    RULE_llamada = 26
    RULE_argumentos = 27
    RULE_indice = 28
    RULE_primario = 29

    ruleNames =  [ "programa", "bloque", "sentencia", "declaracion", "asignacion", 
                   "condicional", "mientras", "para", "funcion", "parametros", 
                   "retorno", "romper", "continuar", "expresion", "disyuncion", 
                   "conjuncion", "negacion", "comparacion", "opRel", "suma", 
                   "opSuma", "producto", "opProd", "unario", "potencia", 
                   "postfijo", "llamada", "argumentos", "indice", "primario" ]

    EOF = Token.EOF
    VARIABLE=1
    SI=2
    ENTONCES=3
    SINO=4
    FIN=5
    MIENTRAS=6
    HACER=7
    PARA=8
    DESDE=9
    HASTA=10
    PASO=11
    FUNCION=12
    RETORNAR=13
    ROMPER=14
    CONTINUAR=15
    VERDADERO=16
    FALSO=17
    NULO=18
    Y=19
    O=20
    NO=21
    IGUAL=22
    DIFERENTE=23
    MENORIGUAL=24
    MAYORIGUAL=25
    MENOR=26
    MAYOR=27
    ASIG=28
    MAS=29
    MENOS=30
    POR=31
    DIV=32
    MOD=33
    POT=34
    PARI=35
    PARD=36
    CORI=37
    CORD=38
    COMA=39
    NUMERO=40
    TEXTO=41
    ID=42
    COMENTARIO=43
    ESPACIO=44
    DESCONOCIDO=45

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(LlanoParser.EOF, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LlanoParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(LlanoParser.SentenciaContext,i)


        def getRuleIndex(self):
            return LlanoParser.RULE_programa

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = LlanoParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7869456445766) != 0):
                self.state = 60
                self.sentencia()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
            self.match(LlanoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LlanoParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(LlanoParser.SentenciaContext,i)


        def getRuleIndex(self):
            return LlanoParser.RULE_bloque

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = LlanoParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7869456445766) != 0):
                self.state = 68
                self.sentencia()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion(self):
            return self.getTypedRuleContext(LlanoParser.DeclaracionContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(LlanoParser.AsignacionContext,0)


        def condicional(self):
            return self.getTypedRuleContext(LlanoParser.CondicionalContext,0)


        def mientras(self):
            return self.getTypedRuleContext(LlanoParser.MientrasContext,0)


        def para(self):
            return self.getTypedRuleContext(LlanoParser.ParaContext,0)


        def funcion(self):
            return self.getTypedRuleContext(LlanoParser.FuncionContext,0)


        def retorno(self):
            return self.getTypedRuleContext(LlanoParser.RetornoContext,0)


        def romper(self):
            return self.getTypedRuleContext(LlanoParser.RomperContext,0)


        def continuar(self):
            return self.getTypedRuleContext(LlanoParser.ContinuarContext,0)


        def expresion(self):
            return self.getTypedRuleContext(LlanoParser.ExpresionContext,0)


        def getRuleIndex(self):
            return LlanoParser.RULE_sentencia

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia" ):
                return visitor.visitSentencia(self)
            else:
                return visitor.visitChildren(self)




    def sentencia(self):

        localctx = LlanoParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sentencia)
        try:
            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.declaracion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.asignacion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 76
                self.condicional()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 77
                self.mientras()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 78
                self.para()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 79
                self.funcion()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 80
                self.retorno()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 81
                self.romper()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 82
                self.continuar()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 83
                self.expresion()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(LlanoParser.VARIABLE, 0)

        def ID(self):
            return self.getToken(LlanoParser.ID, 0)

        def ASIG(self):
            return self.getToken(LlanoParser.ASIG, 0)

        def expresion(self):
            return self.getTypedRuleContext(LlanoParser.ExpresionContext,0)


        def getRuleIndex(self):
            return LlanoParser.RULE_declaracion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion(self):

        localctx = LlanoParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaracion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(LlanoParser.VARIABLE)
            self.state = 87
            self.match(LlanoParser.ID)
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 88
                self.match(LlanoParser.ASIG)
                self.state = 89
                self.expresion()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LlanoParser.ID, 0)

        def ASIG(self):
            return self.getToken(LlanoParser.ASIG, 0)

        def expresion(self):
            return self.getTypedRuleContext(LlanoParser.ExpresionContext,0)


        def indice(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LlanoParser.IndiceContext)
            else:
                return self.getTypedRuleContext(LlanoParser.IndiceContext,i)


        def getRuleIndex(self):
            return LlanoParser.RULE_asignacion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = LlanoParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_asignacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(LlanoParser.ID)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 93
                self.indice()
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 99
            self.match(LlanoParser.ASIG)
            self.state = 100
            self.expresion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SI(self, i:int=None):
            if i is None:
                return self.getTokens(LlanoParser.SI)
            else:
                return self.getToken(LlanoParser.SI, i)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LlanoParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(LlanoParser.ExpresionContext,i)


        def ENTONCES(self, i:int=None):
            if i is None:
                return self.getTokens(LlanoParser.ENTONCES)
            else:
                return self.getToken(LlanoParser.ENTONCES, i)

        def bloque(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LlanoParser.BloqueContext)
            else:
                return self.getTypedRuleContext(LlanoParser.BloqueContext,i)


        def FIN(self):
            return self.getToken(LlanoParser.FIN, 0)

        def SINO(self, i:int=None):
            if i is None:
                return self.getTokens(LlanoParser.SINO)
            else:
                return self.getToken(LlanoParser.SINO, i)

        def getRuleIndex(self):
            return LlanoParser.RULE_condicional

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicional" ):
                return visitor.visitCondicional(self)
            else:
                return visitor.visitChildren(self)




    def condicional(self):

        localctx = LlanoParser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(LlanoParser.SI)
            self.state = 103
            self.expresion()
            self.state = 104
            self.match(LlanoParser.ENTONCES)
            self.state = 105
            self.bloque()
            self.state = 114
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 106
                    self.match(LlanoParser.SINO)
                    self.state = 107
                    self.match(LlanoParser.SI)
                    self.state = 108
                    self.expresion()
                    self.state = 109
                    self.match(LlanoParser.ENTONCES)
                    self.state = 110
                    self.bloque() 
                self.state = 116
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 117
                self.match(LlanoParser.SINO)
                self.state = 118
                self.bloque()


            self.state = 121
            self.match(LlanoParser.FIN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MientrasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MIENTRAS(self):
            return self.getToken(LlanoParser.MIENTRAS, 0)

        def expresion(self):
            return self.getTypedRuleContext(LlanoParser.ExpresionContext,0)


        def HACER(self):
            return self.getToken(LlanoParser.HACER, 0)

        def bloque(self):
            return self.getTypedRuleContext(LlanoParser.BloqueContext,0)


        def FIN(self):
            return self.getToken(LlanoParser.FIN, 0)

        def getRuleIndex(self):
            return LlanoParser.RULE_mientras

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMientras" ):
                return visitor.visitMientras(self)
            else:
                return visitor.visitChildren(self)




    def mientras(self):

        localctx = LlanoParser.MientrasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_mientras)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(LlanoParser.MIENTRAS)
            self.state = 124
            self.expresion()
            self.state = 125
            self.match(LlanoParser.HACER)
            self.state = 126
            self.bloque()
            self.state = 127
            self.match(LlanoParser.FIN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARA(self):
            return self.getToken(LlanoParser.PARA, 0)

        def ID(self):
            return self.getToken(LlanoParser.ID, 0)

        def DESDE(self):
            return self.getToken(LlanoParser.DESDE, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LlanoParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(LlanoParser.ExpresionContext,i)


        def HASTA(self):
            return self.getToken(LlanoParser.HASTA, 0)

        def HACER(self):
            return self.getToken(LlanoParser.HACER, 0)

        def bloque(self):
            return self.getTypedRuleContext(LlanoParser.BloqueContext,0)


        def FIN(self):
            return self.getToken(LlanoParser.FIN, 0)

        def PASO(self):
            return self.getToken(LlanoParser.PASO, 0)

        def getRuleIndex(self):
            return LlanoParser.RULE_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara" ):
                return visitor.visitPara(self)
            else:
                return visitor.visitChildren(self)




    def para(self):

        localctx = LlanoParser.ParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_para)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(LlanoParser.PARA)
            self.state = 130
            self.match(LlanoParser.ID)
            self.state = 131
            self.match(LlanoParser.DESDE)
            self.state = 132
            self.expresion()
            self.state = 133
            self.match(LlanoParser.HASTA)
            self.state = 134
            self.expresion()
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 135
                self.match(LlanoParser.PASO)
                self.state = 136
                self.expresion()


            self.state = 139
            self.match(LlanoParser.HACER)
            self.state = 140
            self.bloque()
            self.state = 141
            self.match(LlanoParser.FIN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCION(self):
            return self.getToken(LlanoParser.FUNCION, 0)

        def ID(self):
            return self.getToken(LlanoParser.ID, 0)

        def PARI(self):
            return self.getToken(LlanoParser.PARI, 0)

        def PARD(self):
            return self.getToken(LlanoParser.PARD, 0)

        def bloque(self):
            return self.getTypedRuleContext(LlanoParser.BloqueContext,0)


        def FIN(self):
            return self.getToken(LlanoParser.FIN, 0)

        def parametros(self):
            return self.getTypedRuleContext(LlanoParser.ParametrosContext,0)


        def getRuleIndex(self):
            return LlanoParser.RULE_funcion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncion" ):
                return visitor.visitFuncion(self)
            else:
                return visitor.visitChildren(self)




    def funcion(self):

        localctx = LlanoParser.FuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_funcion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(LlanoParser.FUNCION)
            self.state = 144
            self.match(LlanoParser.ID)
            self.state = 145
            self.match(LlanoParser.PARI)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 146
                self.parametros()


            self.state = 149
            self.match(LlanoParser.PARD)
            self.state = 150
            self.bloque()
            self.state = 151
            self.match(LlanoParser.FIN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(LlanoParser.ID)
            else:
                return self.getToken(LlanoParser.ID, i)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(LlanoParser.COMA)
            else:
                return self.getToken(LlanoParser.COMA, i)

        def getRuleIndex(self):
            return LlanoParser.RULE_parametros

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametros" ):
                return visitor.visitParametros(self)
            else:
                return visitor.visitChildren(self)




    def parametros(self):

        localctx = LlanoParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_parametros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(LlanoParser.ID)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==39:
                self.state = 154
                self.match(LlanoParser.COMA)
                self.state = 155
                self.match(LlanoParser.ID)
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetornoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETORNAR(self):
            return self.getToken(LlanoParser.RETORNAR, 0)

        def expresion(self):
            return self.getTypedRuleContext(LlanoParser.ExpresionContext,0)


        def getRuleIndex(self):
            return LlanoParser.RULE_retorno

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRetorno" ):
                return visitor.visitRetorno(self)
            else:
                return visitor.visitChildren(self)




    def retorno(self):

        localctx = LlanoParser.RetornoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_retorno)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(LlanoParser.RETORNAR)
            self.state = 162
            self.expresion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RomperContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ROMPER(self):
            return self.getToken(LlanoParser.ROMPER, 0)

        def getRuleIndex(self):
            return LlanoParser.RULE_romper

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRomper" ):
                return visitor.visitRomper(self)
            else:
                return visitor.visitChildren(self)




    def romper(self):

        localctx = LlanoParser.RomperContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_romper)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(LlanoParser.ROMPER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUAR(self):
            return self.getToken(LlanoParser.CONTINUAR, 0)

        def getRuleIndex(self):
            return LlanoParser.RULE_continuar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuar" ):
                return visitor.visitContinuar(self)
            else:
                return visitor.visitChildren(self)




    def continuar(self):

        localctx = LlanoParser.ContinuarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_continuar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(LlanoParser.CONTINUAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def disyuncion(self):
            return self.getTypedRuleContext(LlanoParser.DisyuncionContext,0)


        def getRuleIndex(self):
            return LlanoParser.RULE_expresion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresion" ):
                return visitor.visitExpresion(self)
            else:
                return visitor.visitChildren(self)




    def expresion(self):

        localctx = LlanoParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expresion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.disyuncion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DisyuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conjuncion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LlanoParser.ConjuncionContext)
            else:
                return self.getTypedRuleContext(LlanoParser.ConjuncionContext,i)


        def O(self, i:int=None):
            if i is None:
                return self.getTokens(LlanoParser.O)
            else:
                return self.getToken(LlanoParser.O, i)

        def getRuleIndex(self):
            return LlanoParser.RULE_disyuncion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDisyuncion" ):
                return visitor.visitDisyuncion(self)
            else:
                return visitor.visitChildren(self)




    def disyuncion(self):

        localctx = LlanoParser.DisyuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_disyuncion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.conjuncion()
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 171
                self.match(LlanoParser.O)
                self.state = 172
                self.conjuncion()
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConjuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def negacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LlanoParser.NegacionContext)
            else:
                return self.getTypedRuleContext(LlanoParser.NegacionContext,i)


        def Y(self, i:int=None):
            if i is None:
                return self.getTokens(LlanoParser.Y)
            else:
                return self.getToken(LlanoParser.Y, i)

        def getRuleIndex(self):
            return LlanoParser.RULE_conjuncion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConjuncion" ):
                return visitor.visitConjuncion(self)
            else:
                return visitor.visitChildren(self)




    def conjuncion(self):

        localctx = LlanoParser.ConjuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_conjuncion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.negacion()
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 179
                self.match(LlanoParser.Y)
                self.state = 180
                self.negacion()
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NegacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NO(self):
            return self.getToken(LlanoParser.NO, 0)

        def negacion(self):
            return self.getTypedRuleContext(LlanoParser.NegacionContext,0)


        def comparacion(self):
            return self.getTypedRuleContext(LlanoParser.ComparacionContext,0)


        def getRuleIndex(self):
            return LlanoParser.RULE_negacion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegacion" ):
                return visitor.visitNegacion(self)
            else:
                return visitor.visitChildren(self)




    def negacion(self):

        localctx = LlanoParser.NegacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_negacion)
        try:
            self.state = 189
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.match(LlanoParser.NO)
                self.state = 187
                self.negacion()
                pass
            elif token in [16, 17, 18, 30, 35, 37, 40, 41, 42]:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.comparacion()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def suma(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LlanoParser.SumaContext)
            else:
                return self.getTypedRuleContext(LlanoParser.SumaContext,i)


        def opRel(self):
            return self.getTypedRuleContext(LlanoParser.OpRelContext,0)


        def getRuleIndex(self):
            return LlanoParser.RULE_comparacion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparacion" ):
                return visitor.visitComparacion(self)
            else:
                return visitor.visitChildren(self)




    def comparacion(self):

        localctx = LlanoParser.ComparacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_comparacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.suma()
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 264241152) != 0):
                self.state = 192
                self.opRel()
                self.state = 193
                self.suma()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpRelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IGUAL(self):
            return self.getToken(LlanoParser.IGUAL, 0)

        def DIFERENTE(self):
            return self.getToken(LlanoParser.DIFERENTE, 0)

        def MENOR(self):
            return self.getToken(LlanoParser.MENOR, 0)

        def MAYOR(self):
            return self.getToken(LlanoParser.MAYOR, 0)

        def MENORIGUAL(self):
            return self.getToken(LlanoParser.MENORIGUAL, 0)

        def MAYORIGUAL(self):
            return self.getToken(LlanoParser.MAYORIGUAL, 0)

        def getRuleIndex(self):
            return LlanoParser.RULE_opRel

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpRel" ):
                return visitor.visitOpRel(self)
            else:
                return visitor.visitChildren(self)




    def opRel(self):

        localctx = LlanoParser.OpRelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_opRel)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 264241152) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SumaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def producto(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LlanoParser.ProductoContext)
            else:
                return self.getTypedRuleContext(LlanoParser.ProductoContext,i)


        def opSuma(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LlanoParser.OpSumaContext)
            else:
                return self.getTypedRuleContext(LlanoParser.OpSumaContext,i)


        def getRuleIndex(self):
            return LlanoParser.RULE_suma

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuma" ):
                return visitor.visitSuma(self)
            else:
                return visitor.visitChildren(self)




    def suma(self):

        localctx = LlanoParser.SumaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_suma)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.producto()
            self.state = 205
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 200
                    self.opSuma()
                    self.state = 201
                    self.producto() 
                self.state = 207
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpSumaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAS(self):
            return self.getToken(LlanoParser.MAS, 0)

        def MENOS(self):
            return self.getToken(LlanoParser.MENOS, 0)

        def getRuleIndex(self):
            return LlanoParser.RULE_opSuma

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpSuma" ):
                return visitor.visitOpSuma(self)
            else:
                return visitor.visitChildren(self)




    def opSuma(self):

        localctx = LlanoParser.OpSumaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_opSuma)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            _la = self._input.LA(1)
            if not(_la==29 or _la==30):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProductoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unario(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LlanoParser.UnarioContext)
            else:
                return self.getTypedRuleContext(LlanoParser.UnarioContext,i)


        def opProd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LlanoParser.OpProdContext)
            else:
                return self.getTypedRuleContext(LlanoParser.OpProdContext,i)


        def getRuleIndex(self):
            return LlanoParser.RULE_producto

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProducto" ):
                return visitor.visitProducto(self)
            else:
                return visitor.visitChildren(self)




    def producto(self):

        localctx = LlanoParser.ProductoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_producto)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.unario()
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 15032385536) != 0):
                self.state = 211
                self.opProd()
                self.state = 212
                self.unario()
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpProdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POR(self):
            return self.getToken(LlanoParser.POR, 0)

        def DIV(self):
            return self.getToken(LlanoParser.DIV, 0)

        def MOD(self):
            return self.getToken(LlanoParser.MOD, 0)

        def getRuleIndex(self):
            return LlanoParser.RULE_opProd

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpProd" ):
                return visitor.visitOpProd(self)
            else:
                return visitor.visitChildren(self)




    def opProd(self):

        localctx = LlanoParser.OpProdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_opProd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15032385536) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnarioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MENOS(self):
            return self.getToken(LlanoParser.MENOS, 0)

        def unario(self):
            return self.getTypedRuleContext(LlanoParser.UnarioContext,0)


        def potencia(self):
            return self.getTypedRuleContext(LlanoParser.PotenciaContext,0)


        def getRuleIndex(self):
            return LlanoParser.RULE_unario

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnario" ):
                return visitor.visitUnario(self)
            else:
                return visitor.visitChildren(self)




    def unario(self):

        localctx = LlanoParser.UnarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_unario)
        try:
            self.state = 224
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.match(LlanoParser.MENOS)
                self.state = 222
                self.unario()
                pass
            elif token in [16, 17, 18, 35, 37, 40, 41, 42]:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
                self.potencia()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PotenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def postfijo(self):
            return self.getTypedRuleContext(LlanoParser.PostfijoContext,0)


        def POT(self):
            return self.getToken(LlanoParser.POT, 0)

        def unario(self):
            return self.getTypedRuleContext(LlanoParser.UnarioContext,0)


        def getRuleIndex(self):
            return LlanoParser.RULE_potencia

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPotencia" ):
                return visitor.visitPotencia(self)
            else:
                return visitor.visitChildren(self)




    def potencia(self):

        localctx = LlanoParser.PotenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_potencia)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.postfijo()
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 227
                self.match(LlanoParser.POT)
                self.state = 228
                self.unario()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostfijoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primario(self):
            return self.getTypedRuleContext(LlanoParser.PrimarioContext,0)


        def llamada(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LlanoParser.LlamadaContext)
            else:
                return self.getTypedRuleContext(LlanoParser.LlamadaContext,i)


        def indice(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LlanoParser.IndiceContext)
            else:
                return self.getTypedRuleContext(LlanoParser.IndiceContext,i)


        def getRuleIndex(self):
            return LlanoParser.RULE_postfijo

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfijo" ):
                return visitor.visitPostfijo(self)
            else:
                return visitor.visitChildren(self)




    def postfijo(self):

        localctx = LlanoParser.PostfijoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_postfijo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.primario()
            self.state = 236
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 234
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [35]:
                        self.state = 232
                        self.llamada()
                        pass
                    elif token in [37]:
                        self.state = 233
                        self.indice()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 238
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlamadaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARI(self):
            return self.getToken(LlanoParser.PARI, 0)

        def PARD(self):
            return self.getToken(LlanoParser.PARD, 0)

        def argumentos(self):
            return self.getTypedRuleContext(LlanoParser.ArgumentosContext,0)


        def getRuleIndex(self):
            return LlanoParser.RULE_llamada

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamada" ):
                return visitor.visitLlamada(self)
            else:
                return visitor.visitChildren(self)




    def llamada(self):

        localctx = LlanoParser.LlamadaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_llamada)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(LlanoParser.PARI)
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7869456384000) != 0):
                self.state = 240
                self.argumentos()


            self.state = 243
            self.match(LlanoParser.PARD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LlanoParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(LlanoParser.ExpresionContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(LlanoParser.COMA)
            else:
                return self.getToken(LlanoParser.COMA, i)

        def getRuleIndex(self):
            return LlanoParser.RULE_argumentos

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentos" ):
                return visitor.visitArgumentos(self)
            else:
                return visitor.visitChildren(self)




    def argumentos(self):

        localctx = LlanoParser.ArgumentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_argumentos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.expresion()
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==39:
                self.state = 246
                self.match(LlanoParser.COMA)
                self.state = 247
                self.expresion()
                self.state = 252
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndiceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CORI(self):
            return self.getToken(LlanoParser.CORI, 0)

        def expresion(self):
            return self.getTypedRuleContext(LlanoParser.ExpresionContext,0)


        def CORD(self):
            return self.getToken(LlanoParser.CORD, 0)

        def getRuleIndex(self):
            return LlanoParser.RULE_indice

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndice" ):
                return visitor.visitIndice(self)
            else:
                return visitor.visitChildren(self)




    def indice(self):

        localctx = LlanoParser.IndiceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_indice)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(LlanoParser.CORI)
            self.state = 254
            self.expresion()
            self.state = 255
            self.match(LlanoParser.CORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimarioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LlanoParser.RULE_primario

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TextoContext(PrimarioContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LlanoParser.PrimarioContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TEXTO(self):
            return self.getToken(LlanoParser.TEXTO, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTexto" ):
                return visitor.visitTexto(self)
            else:
                return visitor.visitChildren(self)


    class ListaContext(PrimarioContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LlanoParser.PrimarioContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CORI(self):
            return self.getToken(LlanoParser.CORI, 0)
        def CORD(self):
            return self.getToken(LlanoParser.CORD, 0)
        def argumentos(self):
            return self.getTypedRuleContext(LlanoParser.ArgumentosContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista" ):
                return visitor.visitLista(self)
            else:
                return visitor.visitChildren(self)


    class AgrupacionContext(PrimarioContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LlanoParser.PrimarioContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PARI(self):
            return self.getToken(LlanoParser.PARI, 0)
        def expresion(self):
            return self.getTypedRuleContext(LlanoParser.ExpresionContext,0)

        def PARD(self):
            return self.getToken(LlanoParser.PARD, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAgrupacion" ):
                return visitor.visitAgrupacion(self)
            else:
                return visitor.visitChildren(self)


    class NumeroContext(PrimarioContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LlanoParser.PrimarioContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMERO(self):
            return self.getToken(LlanoParser.NUMERO, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumero" ):
                return visitor.visitNumero(self)
            else:
                return visitor.visitChildren(self)


    class LogicoContext(PrimarioContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LlanoParser.PrimarioContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VERDADERO(self):
            return self.getToken(LlanoParser.VERDADERO, 0)
        def FALSO(self):
            return self.getToken(LlanoParser.FALSO, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogico" ):
                return visitor.visitLogico(self)
            else:
                return visitor.visitChildren(self)


    class NuloContext(PrimarioContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LlanoParser.PrimarioContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NULO(self):
            return self.getToken(LlanoParser.NULO, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNulo" ):
                return visitor.visitNulo(self)
            else:
                return visitor.visitChildren(self)


    class IdentificadorContext(PrimarioContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LlanoParser.PrimarioContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LlanoParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentificador" ):
                return visitor.visitIdentificador(self)
            else:
                return visitor.visitChildren(self)



    def primario(self):

        localctx = LlanoParser.PrimarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_primario)
        self._la = 0 # Token type
        try:
            self.state = 271
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                localctx = LlanoParser.NumeroContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.match(LlanoParser.NUMERO)
                pass
            elif token in [41]:
                localctx = LlanoParser.TextoContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 258
                self.match(LlanoParser.TEXTO)
                pass
            elif token in [16, 17]:
                localctx = LlanoParser.LogicoContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 259
                _la = self._input.LA(1)
                if not(_la==16 or _la==17):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [18]:
                localctx = LlanoParser.NuloContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 260
                self.match(LlanoParser.NULO)
                pass
            elif token in [42]:
                localctx = LlanoParser.IdentificadorContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 261
                self.match(LlanoParser.ID)
                pass
            elif token in [37]:
                localctx = LlanoParser.ListaContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 262
                self.match(LlanoParser.CORI)
                self.state = 264
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7869456384000) != 0):
                    self.state = 263
                    self.argumentos()


                self.state = 266
                self.match(LlanoParser.CORD)
                pass
            elif token in [35]:
                localctx = LlanoParser.AgrupacionContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 267
                self.match(LlanoParser.PARI)
                self.state = 268
                self.expresion()
                self.state = 269
                self.match(LlanoParser.PARD)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






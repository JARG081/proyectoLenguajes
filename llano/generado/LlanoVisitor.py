# Generated from /home/claude/llano/gramatica/Llano.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LlanoParser import LlanoParser
else:
    from LlanoParser import LlanoParser

# This class defines a complete generic visitor for a parse tree produced by LlanoParser.

class LlanoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LlanoParser#programa.
    def visitPrograma(self, ctx:LlanoParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LlanoParser#bloque.
    def visitBloque(self, ctx:LlanoParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LlanoParser#sentencia.
    def visitSentencia(self, ctx:LlanoParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LlanoParser#declaracion.
    def visitDeclaracion(self, ctx:LlanoParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LlanoParser#asignacion.
    def visitAsignacion(self, ctx:LlanoParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LlanoParser#condicional.
    def visitCondicional(self, ctx:LlanoParser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LlanoParser#mientras.
    def visitMientras(self, ctx:LlanoParser.MientrasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LlanoParser#para.
    def visitPara(self, ctx:LlanoParser.ParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LlanoParser#funcion.
    def visitFuncion(self, ctx:LlanoParser.FuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LlanoParser#parametros.
    def visitParametros(self, ctx:LlanoParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LlanoParser#retorno.
    def visitRetorno(self, ctx:LlanoParser.RetornoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LlanoParser#expresion.
    def visitExpresion(self, ctx:LlanoParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LlanoParser#disyuncion.
    def visitDisyuncion(self, ctx:LlanoParser.DisyuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LlanoParser#conjuncion.
    def visitConjuncion(self, ctx:LlanoParser.ConjuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LlanoParser#negacion.
    def visitNegacion(self, ctx:LlanoParser.NegacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LlanoParser#comparacion.
    def visitComparacion(self, ctx:LlanoParser.ComparacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LlanoParser#opRel.
    def visitOpRel(self, ctx:LlanoParser.OpRelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LlanoParser#suma.
    def visitSuma(self, ctx:LlanoParser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LlanoParser#opSuma.
    def visitOpSuma(self, ctx:LlanoParser.OpSumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LlanoParser#producto.
    def visitProducto(self, ctx:LlanoParser.ProductoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LlanoParser#opProd.
    def visitOpProd(self, ctx:LlanoParser.OpProdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LlanoParser#unario.
    def visitUnario(self, ctx:LlanoParser.UnarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LlanoParser#potencia.
    def visitPotencia(self, ctx:LlanoParser.PotenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LlanoParser#postfijo.
    def visitPostfijo(self, ctx:LlanoParser.PostfijoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LlanoParser#llamada.
    def visitLlamada(self, ctx:LlanoParser.LlamadaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LlanoParser#argumentos.
    def visitArgumentos(self, ctx:LlanoParser.ArgumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LlanoParser#indice.
    def visitIndice(self, ctx:LlanoParser.IndiceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LlanoParser#numero.
    def visitNumero(self, ctx:LlanoParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LlanoParser#texto.
    def visitTexto(self, ctx:LlanoParser.TextoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LlanoParser#logico.
    def visitLogico(self, ctx:LlanoParser.LogicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LlanoParser#nulo.
    def visitNulo(self, ctx:LlanoParser.NuloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LlanoParser#identificador.
    def visitIdentificador(self, ctx:LlanoParser.IdentificadorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LlanoParser#lista.
    def visitLista(self, ctx:LlanoParser.ListaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LlanoParser#agrupacion.
    def visitAgrupacion(self, ctx:LlanoParser.AgrupacionContext):
        return self.visitChildren(ctx)



del LlanoParser
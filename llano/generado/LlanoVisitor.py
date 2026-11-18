from antlr4 import *
if "." in __name__:
    from .LlanoParser import LlanoParser
else:
    from LlanoParser import LlanoParser


class LlanoVisitor(ParseTreeVisitor):

    def visitPrograma(self, ctx:LlanoParser.ProgramaContext):
        return self.visitChildren(ctx)


    def visitBloque(self, ctx:LlanoParser.BloqueContext):
        return self.visitChildren(ctx)


    def visitSentencia(self, ctx:LlanoParser.SentenciaContext):
        return self.visitChildren(ctx)


    def visitDeclaracion(self, ctx:LlanoParser.DeclaracionContext):
        return self.visitChildren(ctx)


    def visitAsignacion(self, ctx:LlanoParser.AsignacionContext):
        return self.visitChildren(ctx)


    def visitCondicional(self, ctx:LlanoParser.CondicionalContext):
        return self.visitChildren(ctx)


    def visitMientras(self, ctx:LlanoParser.MientrasContext):
        return self.visitChildren(ctx)


    def visitPara(self, ctx:LlanoParser.ParaContext):
        return self.visitChildren(ctx)


    def visitFuncion(self, ctx:LlanoParser.FuncionContext):
        return self.visitChildren(ctx)


    def visitParametros(self, ctx:LlanoParser.ParametrosContext):
        return self.visitChildren(ctx)


    def visitRetorno(self, ctx:LlanoParser.RetornoContext):
        return self.visitChildren(ctx)


    def visitRomper(self, ctx:LlanoParser.RomperContext):
        return self.visitChildren(ctx)


    def visitContinuar(self, ctx:LlanoParser.ContinuarContext):
        return self.visitChildren(ctx)


    def visitExpresion(self, ctx:LlanoParser.ExpresionContext):
        return self.visitChildren(ctx)


    def visitDisyuncion(self, ctx:LlanoParser.DisyuncionContext):
        return self.visitChildren(ctx)


    def visitConjuncion(self, ctx:LlanoParser.ConjuncionContext):
        return self.visitChildren(ctx)


    def visitNegacion(self, ctx:LlanoParser.NegacionContext):
        return self.visitChildren(ctx)


    def visitComparacion(self, ctx:LlanoParser.ComparacionContext):
        return self.visitChildren(ctx)


    def visitOpRel(self, ctx:LlanoParser.OpRelContext):
        return self.visitChildren(ctx)


    def visitSuma(self, ctx:LlanoParser.SumaContext):
        return self.visitChildren(ctx)


    def visitOpSuma(self, ctx:LlanoParser.OpSumaContext):
        return self.visitChildren(ctx)


    def visitProducto(self, ctx:LlanoParser.ProductoContext):
        return self.visitChildren(ctx)


    def visitOpProd(self, ctx:LlanoParser.OpProdContext):
        return self.visitChildren(ctx)


    def visitUnario(self, ctx:LlanoParser.UnarioContext):
        return self.visitChildren(ctx)


    def visitPotencia(self, ctx:LlanoParser.PotenciaContext):
        return self.visitChildren(ctx)


    def visitPostfijo(self, ctx:LlanoParser.PostfijoContext):
        return self.visitChildren(ctx)


    def visitLlamada(self, ctx:LlanoParser.LlamadaContext):
        return self.visitChildren(ctx)


    def visitArgumentos(self, ctx:LlanoParser.ArgumentosContext):
        return self.visitChildren(ctx)


    def visitIndice(self, ctx:LlanoParser.IndiceContext):
        return self.visitChildren(ctx)


    def visitNumero(self, ctx:LlanoParser.NumeroContext):
        return self.visitChildren(ctx)


    def visitTexto(self, ctx:LlanoParser.TextoContext):
        return self.visitChildren(ctx)


    def visitLogico(self, ctx:LlanoParser.LogicoContext):
        return self.visitChildren(ctx)


    def visitNulo(self, ctx:LlanoParser.NuloContext):
        return self.visitChildren(ctx)


    def visitIdentificador(self, ctx:LlanoParser.IdentificadorContext):
        return self.visitChildren(ctx)


    def visitLista(self, ctx:LlanoParser.ListaContext):
        return self.visitChildren(ctx)

    def visitAgrupacion(self, ctx:LlanoParser.AgrupacionContext):
        return self.visitChildren(ctx)



del LlanoParser
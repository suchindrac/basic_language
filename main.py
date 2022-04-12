from antlr4 import *
from dist.BasicLangLexer import BasicLangLexer
from dist.BasicLangVisitor import BasicLangVisitor
from dist.BasicLangVisitor import BasicLangVisitor
from dist.BasicLangParser import BasicLangParser
import sys

class MyVisitor(BasicLangVisitor):
    def visitShow(self, ctx):
        if ctx.INT() != None:
            return ctx.INT()
        if ctx.ID() != None:
            id = ctx.ID().getText()
    
            try:
                return globals()[id]
            except:
                return id

    def visitQuit(self, ctx):
        print("Bye")
        sys.exit(1)

    def visitExprEqn(self, ctx):
        var = ctx.var.text
        value = ctx.value
        if isinstance(value, BasicLangParser.InfixExprContext):
            value = self.visit(value)
        if isinstance(value, BasicLangParser.ParenExprContext):
            value = self.visit(value)

        globals()[var] = value

        return f"{var} set to {value}"

    def visitEqn(self, ctx):
        var = ctx.var.text
        value = ctx.value
        value = value.text
        
        try:
            value = int(value)
        except:
            pass

        globals()[var] = value
        return f"Set {var} to {value}"

    def visitNumberExpr(self, ctx):
        value = ctx.getText()
        return int(value)

    def visitIDExpr(self, ctx):
        value = ctx.getText()
        if value in globals().keys():
            return globals()[value]
        else:
            return f"Variable {value} not defined"

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitInfixExpr(self, ctx):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        op = ctx.op.text

        operation =  {
        '+': lambda: l + r,
        '-': lambda: l - r,
        '*': lambda: l * r,
        '/': lambda: l / r,
        }
        return operation.get(op, lambda: None)()

def main():
    while True:
        lexer = BasicLangLexer(InputStream(input(">>> ")))
        stream = CommonTokenStream(lexer)
        parser = BasicLangParser(stream)
        tree = parser.statement()
        visitor = MyVisitor()
        output = visitor.visit(tree)
        print(output)

if __name__ == '__main__':
    main()

source run.sh

antlr4 -Dlanguage=Python3 MyGrammer.g4 -visitor -o dist

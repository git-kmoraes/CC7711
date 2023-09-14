progenitor(antonia, joão).
progenitor(pedro, joão).
progenitor(antonia, clara).
progenitor(pedro, clara).
progenitor(antonia, francisco).
progenitor(pedro, francisco).
progenitor(antonia, ana).
progenitor(pedro, ana).
progenitor(ana, helena).
progenitor(ana, joana).
progenitor(joão, mario).
progenitor(helena, carlos).
progenitor(mario, carlos).
progenitor(clara, pietro).
progenitor(clara, enzo).

casados(pedro, antonia).
casados(franscisco, milene).

sexo(antonia, feminino).
sexo(pedro, masculino).
sexo(joão, masculino).
sexo(clara, feminino).
sexo(francisco, masculino).
sexo(ana, feminino).
sexo(helena, feminino).
sexo(joana, feminino).
sexo(mario, masculino).
sexo(carlos, masculino).
sexo(pietro, masculino).
sexo(enzo, masculino).
sexo(milene, feminino).
sexo(franscisca, feminino).

irma(X,Y):- progenitor(A,X),
progenitor(A,Y),
X\==Y,
sexo(X,feminino).

irmao(X,Y):- progenitor(A,X),
progenitor(A,Y),
X\==Y,
sexo(X,masculino).

avo(X,Y):- progenitor(X,A),
progenitor(A,Y),
sexo(X,masculino).

ava(X,Y):- progenitor(X,A),
progenitor(A,Y),
sexo(X,feminino).

tio(X,Y):- progenitor(A,Y), irmao(X,A).
tia(X,Y):- progenitor(A,Y), irma(X,A).

primo(X, Y) :- progenitor(A, X), progenitor(B, Y), irmao(A, B).
prima(X, Y) :- progenitor(A, X), progenitor(B, Y), irma(A, B).

descendente(X, Y) :- progenitor(Y, X).
ascendente(X, Y) :- descendente(Y, X).
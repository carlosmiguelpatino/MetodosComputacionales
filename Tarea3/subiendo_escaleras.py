import sys

n = sys.argv[1]
posibilidades = 0


"""La solucion al problema es crear una serie de fibonacci porque
para saber las posibilidades hasta un escalón n se deben tener en cuenta
las posibilidades de llegar al anterior escalón y sumarlas. Tomando
este principio desde el escalón uno se obtiene una serie de fibonacci
ya que las posibilidades que hay para llegar un escalón n depende de
las posibilidades de llegar a los dos escalones anteriores. Se toman los
dos escalones anteriores ya que solo se pueden subir uno o dos
escalones a la vez."""

if n == 0:
	print "No hay escalones para subir"

if n == 1:
	print "Hay una "



print "Hay ",posibilidades, "de subir una escalera de ", n, "escalones"
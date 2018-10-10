# coding=utf-8

def SacaDivisores (n):

  limit = int(n**0.5)
  # Sacamos su ra�z cuadrada  
  # Todos los divisores de un n�mero est�n por debajo de su ra�z cuadrada m�s los complementarios de estos que est�n por encima
  # Si el n tiene ra�z cuadrada entera no hay que a�adir el complementario pues estar�a repetido
  # No es necesario recorrer todos los numeros comprendidos entre n y 1 para la b�squeda de divisores, y el uno tampoco pues siempre lo es y lo podemos dar por incluido
  # Hacemos el recorrido de mayor a menor para en cuanto d� la suma de divisores mayor que n poder terminar afirmando que es abusivo
  # Para el caso de n�mero perfectos o defectivos estamos obligados a buscar todos los divisores

  TotalDivisor=1
  # El 1 siempre es divisor
  
  # El 1 no lo comprobamos
  while (limit>1):
    cociente = n % limit
    if not cociente:
      TotalDivisor=TotalDivisor + limit
      complementari=n//limit
      if (complementari != limit):
          # Test para ra�z cuadra existente
          # A�adimos el Complementario
          TotalDivisor=TotalDivisor+(complementari)
    if (TotalDivisor>n):
    	# Si TotalDivisor ya es m�s que n ya podemos afirmar que es abundante y terminar la b�squeda de divisores 
      limit=1
 
    limit=limit-1

  return TotalDivisor


def TestearLista (n):
	TotalDivisores=SacaDivisores(n)
	if (TotalDivisores<n):
	  print "El n�mero:", n, "es defectivo"
	elif (TotalDivisores==n):
	  print "El n�mero:", n, "es perfecto"
	else:
	  print "El n�mero:", n, "es abundante"

	print "\tTotal suma divisores:", TotalDivisores

# LISTA DE N�MEROS A TESTEAR
n=[2460153000341, 246015300034, 500000050, 33550336, 8128, 954, 144, 6]


for i in n:
    TestearLista(i)
    print("\n")

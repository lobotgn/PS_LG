# coding=utf-8

def SacaDivisores (n):

  limit = int(n**0.5)
  # Sacamos su raíz cuadrada  
  # Todos los divisores de un número están por debajo de su raíz cuadrada más los complementarios de estos que están por encima
  # Si el n tiene raíz cuadrada entera no hay que añadir el complementario pues estaría repetido
  # No es necesario recorrer todos los numeros comprendidos entre n y 1 para la búsqueda de divisores, y el uno tampoco pues siempre lo es y lo podemos dar por incluido
  # Hacemos el recorrido de mayor a menor para en cuanto dé la suma de divisores mayor que n poder terminar afirmando que es abusivo
  # Para el caso de número perfectos o defectivos estamos obligados a buscar todos los divisores

  TotalDivisor=1
  # El 1 siempre es divisor
  
  # El 1 no lo comprobamos
  while (limit>1):
    cociente = n % limit
    if not cociente:
      TotalDivisor=TotalDivisor + limit
      complementari=n//limit
      if (complementari != limit):
          # Test para raíz cuadra existente
          # Añadimos el Complementario
          TotalDivisor=TotalDivisor+(complementari)
    if (TotalDivisor>n):
    	# Si TotalDivisor ya es más que n ya podemos afirmar que es abundante y terminar la búsqueda de divisores 
      limit=1
 
    limit=limit-1

  return TotalDivisor


def TestearLista (n):
	TotalDivisores=SacaDivisores(n)
	if (TotalDivisores<n):
	  print "El número:", n, "es defectivo"
	elif (TotalDivisores==n):
	  print "El número:", n, "es perfecto"
	else:
	  print "El número:", n, "es abundante"

	print "\tTotal suma divisores:", TotalDivisores

# LISTA DE NÚMEROS A TESTEAR
n=[2460153000341, 246015300034, 500000050, 33550336, 8128, 954, 144, 6]


for i in n:
    TestearLista(i)
    print("\n")

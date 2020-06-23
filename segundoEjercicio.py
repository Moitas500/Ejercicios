def multiplosDeTres(lista,matriz):
  if lista == []:
      return matriz
  else:
    return multiplosDeTres(lista[1:], matriz + [dividirNumero(lista[0])])

def dividirNumero(sublista):
    if sublista >= 10:
      return dividirNumero(sublista//10) + [3*(sublista%10)]
    return [3*sublista]  

print(multiplosDeTres([685,456], []))



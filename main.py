# Escriba un programa que tenga dos listas y que, a continuación, cree las siguientes listas(en las que no debe haber
# repeticiones):
# - Lista de palabras que aparecen en las dos listas.
# - Lista de palabras que aparecen en la primera lista, pero no en la segunda.
# - Lista de palabras que aparecen en la segunda lista, pero no en la primera.
# - Lista de palabras que aparecen en ambas listas.

lista1 = ['Arroz', 'Sal', 'Azúcar', 'Café', 'Leche', 'Sal', 'Queso', 'Aceite', 'Arroz', 'Carne', 'Atún', 'Azúcar']
lista2 = ['Miel', 'Atún', 'Lenteja', 'Azúcar', 'Miel', 'Carne', 'Lenteja', 'Papa', 'Sal', 'Chocolate', 'Cereal', 'Papa']

# - Lista de palabras que aparecen en las dos listas.

# lista1
setlista1 = set(lista1)
print(f'\nPalabras no repetidas de la primera lista:\n{setlista1}')

# lista2
setlista2 = set(lista2)
print(f'\nPalabras no repetidas de la segunda lista:\n{setlista2}')

# lista1 + lista2
union = setlista1.union(setlista2)
print(f'\nLas palabras que aparecen en las dos listas son:\n{union}')

# - Lista de palabras que aparecen en la primera lista, pero no en la segunda.

result = (setlista1 - setlista2)
print(f'\nPalabras únicas de la primera lista:\n{result}')

# - Lista de palabras que aparecen en la segunda lista, pero no en la primera.

result = (setlista2 - setlista1)
print(f'\nPalabras únicas de la segunda lista:\n{result}')

# - Lista de palabras que aparecen en ambas listas.
result = setlista1.intersection(setlista2)
print(f'\nPalabras en ambas listas:\n{result}')

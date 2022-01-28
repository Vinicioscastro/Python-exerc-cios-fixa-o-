nome = input('Digite algo: ')

print('O tipo disso e :', type(nome))
print('contem apenas spaços? ', nome.isspace())
print('e um numero? ', nome.isnumeric())
print('e alfabeto? ', nome.isalpha())
print('está em minusculas? ', nome.islower())
print('está em maisuculas? ', nome.isupper() )
print('está capitalizada? ', nome.istitle())
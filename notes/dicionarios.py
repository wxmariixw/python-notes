# Dicionário
## dicionário acessa por chaves {}
planet = {
    "name": "Earth",
    "moons": 1
}

# get() - Usa-se para ler os valores de respectivas chaves do dicionário
name = planet.get("name")
print(name)

# update() - Modifica o valor da chave de um dicionário
planet.update({'name': 'Makemake'})
print(planet)

## Ao adicionar uma chave e um valor à ela também é possível alterar o dicionário
planet['orbital period'] = 4333
print(planet)
 
# pop() - retira a chave e seus valores contidos
planet.pop('orbital period')
print(planet)
 
# keys() - Pra recuperar chaves
rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

for key in rainfall.keys():
    print(key)

# Dados complexos - quando o dado tem uma chave dentro de outra chave
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}

print(planet['diameter (km)'])
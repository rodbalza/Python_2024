import mod

keys, values = mod.get_population()
print(keys, values)

data = [
    {'Country':'España', 'Population': 38},
    {'Country': 'Portugal', 'Population':35}
]

result = mod.population_by_country(data, 'España')
print(result)
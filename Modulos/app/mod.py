def get_population():
    keys = ['Esp', 'Por']
    values = [38, 35]
    return keys, values

def population_by_country(data, country):
    result = list(filter(lambda item:item['Country']==country, data))
    return result
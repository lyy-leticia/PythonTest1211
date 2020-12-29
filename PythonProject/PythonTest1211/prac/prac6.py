x = True
country_counter = {}#字典
print(country_counter)
def addone(country):
    if country in country_counter:
        country_counter[country] += 1
        print("nih",country_counter[country])
    else:
        country_counter[country] = 1
        print(country_counter[country])

addone('China')
addone('Japan')
addone('china')
print(country_counter)
print(len(country_counter))
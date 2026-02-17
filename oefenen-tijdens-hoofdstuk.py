
nummers = [2,5,7,11,15]
print(nummers[0])
print(nummers[-2])
print(nummers.index(11))
nummers[0] = 3
print(nummers)
print(nummers[0] + nummers[1])
print(nummers[2] * nummers[3]) #7*11 = 77

som = 0
for num in nummers:
    som += num
print(som)
print(3+5+7+11+15)

print(sum(nummers))

# list functions

tafel_van_drie = [3,6,9,12,16,18,24,27,32]
print(tafel_van_drie)
tafel_van_drie[4] = 15
print(tafel_van_drie)
tafel_van_drie.remove(32)
print(tafel_van_drie)
tafel_van_drie.append(30)
print(tafel_van_drie)
tafel_van_drie.insert(6,21)
print(tafel_van_drie)

tafel_van_drie.reverse()
print(tafel_van_drie)

# Slicing
namen = ['Alfred', 'Bob', 'Charlie', 'David', 'Erik']
print(namen[:3])
namen[-2:] = ["Daphne", "Eva", "Frederique"]
print(namen)

#list comprehension
list1 = [getal for getal in range(1,21) if getal % 2 == 0]
print(list1)

####################################### TUPLES
var1 = ('rood',)
var2 = ('geel')
print(type(var1))
print(type(var2))
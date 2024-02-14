#day 6 - 30 Day challenge: Tuples
empty_tuple = tuple()
print(empty_tuple)
tuple1_sisters = ('Jane','Doe')
print(tuple1_sisters)
tuple_brothers = ('Jim','Bob')
print(tuple_brothers)
tuple_siblings = tuple1_sisters+tuple_brothers
print(tuple_siblings)
print(len(tuple_siblings))
tuple_parents = ('Jan','Dan')
tuple_siblings = tuple_siblings +tuple_parents 
print(tuple_siblings)
tuple_family_members = tuple_siblings
tuple_siblings = tuple_family_members[0:4]
tuple_parents = tuple_family_members[4:]
print(tuple_siblings)
print(tuple_parents)
fruit = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal_products = ('beef','pork','chicken')
food_stuff_tp = fruit+vegetables+animal_products
food_stuff_tp = list(food_stuff_tp)
middle_point = len(food_stuff_tp)//2
food_mid = food_stuff_tp[middle_point]
food_first_three = food_stuff_tp[:3]
food_last_three = food_stuff_tp[(len(food_stuff_tp)-4):]
print(food_mid)
print(food_first_three)
print(food_last_three)
food_last_three = tuple(food_last_three)
print(food_last_three.index('chicken'))
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
nordic_countries = list(nordic_countries)
exists = nordic_countries.count('Estonia')
print(exists)
print(nordic_countries.count('Iceland'))
#day 12 - 30 Day challenge: List Comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
not_pos_nums = list(filter(lambda x: x<= 0, numbers))
print(not_pos_nums)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
new_list_of_lists = [ k for i in list_of_lists for j in i for k in j]
print(new_list_of_lists)

powers = [(i,i**0,i**1,i**2,i**3,i**4,i**5) for i in range(11)]
print(powers)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new_countries = [[i[0].upper(),i[0][0].upper()+i[0][1].upper()+i[0][2].upper(),i[1].upper()] for j in countries for i in j]
print(new_countries)

dict_countries = [{'Country:' : i[0], 'City:' : i[1]}for j in countries for i in j]
print(dict_countries)

names = [[('Aidan', 'C')], [('David', 'Smith')], [('Joe', 'Random')], [('Bill', 'Gates')]]
names_strs = [[i[0]+' '+i[1]] for j in names for i in j]
print(names_strs)
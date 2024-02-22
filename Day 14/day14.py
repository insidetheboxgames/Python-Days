#day 14 - 30 Day challenge: List Comprehension

# map: built in function that takes a function and an iterable as parameters
# Think iterating over a list
# Filter: Returns a boolean for each item of the specified iterable[List]
# Filters the items that satisfy the filing criteria
# Reduce: Takes two parameters just like map and filter, however it returns a single value.
# Think sumation

# Higher Order Function: Is either a function that takes one or more functions as a parameter
# a function that can be returned as a result of another function
# a function that can be modified, or a function cna be assigned to a variable
# Closure: a nested function to access the outer scope of the enclosing function
# Decorators: a design pattern that allows a user to add new functionality to an existing object
# without modifying its stucture.

# A call function is a function that is being passed into an function like map,filter,or reduce
import functools

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in countries:
    print(i)
for i in names:
    print(i)
for i in numbers:
    print(i)

upperCase_countries = map(lambda country: country.upper(), countries)
print(list(upperCase_countries))

square_Numbers = map(lambda num: num**2, numbers)
print(list(square_Numbers))

upperCase_names = map(lambda name: name.upper(), names)
print(list(upperCase_names))

no_land = filter(lambda country: country.find('land') == -1, countries)
print(list(no_land))

six_letter_countries = filter(lambda country: len(country) == 6, countries)
print(list(six_letter_countries))

six_or_more = filter(lambda country: len(country) >= 6, countries)
print(list(six_or_more))

start_with_E = filter(lambda country: country[0] == 'E', countries)
print(list(start_with_E))

new_numbers = functools.reduce(lambda num,b: num+b, map(lambda num: num**2, filter(lambda num: num>5,numbers)))
print(new_numbers)
print(list(map(lambda num: num**2, filter(lambda num: num>5,numbers))))

def get_string_lists(lst):
    new_lst = filter(lambda is_str: type(is_str) == str, lst)
    return list(new_lst)
test_str = ['ABC',132,'CDE','EFG',51,'z']
print(get_string_lists(test_str))

summation = functools.reduce(lambda x,y: x+y, numbers)
print(summation)

country_sentance = functools.reduce(lambda x,y: x+', '+y, countries)+' are north European countries'
print(country_sentance)
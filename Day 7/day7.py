#day 7 - 30 Day challenge: Sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
it_companies.update(['Samsung','NVIDIA','AMD'])
print(it_companies)
# Throws an error if 'Twitter' does not exist
it_companies.remove('Twitter')
print(it_companies)
# Will not throw an error if this does not exist
it_companies.discard('X')

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
C = A.union(B)
print(C)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
C_withA_B = A.union(B)
C_withB_A = B.union(A)
print(B.symmetric_difference(A))
del A
del B

age = [22, 19, 24, 25, 26, 24, 25, 24]
s_age = set(age)
print('The length of the list is: ',len(age),' The length of the set is: ',len(s_age))

# Strings are arrays of char variables
# list are ordered and changeable collection
# tuple is a ordered and unchangeable collection
# set is unordered and unmodifiable but can have new items added, and no duplicate members

str1 = 'I am a teacher and I love to inspire and teach people'
str_set = str1.split()
print(str_set)
# str_set is all the words that are in the str1
str_set = set(str_set)
print(str_set)

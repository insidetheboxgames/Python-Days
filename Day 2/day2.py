#Day 2 - 30 Day Challenge: Variables
first_name = 'f_name'
last_name = 'l_name'
full_name = 'ful_name'
country = 'Country'
city = 'city'
age = 19
year = 2024
is_married = False
is_light_on = True
day,date,year = 'Friday', '2/9/2024', '2024'

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_light_on))
print(type(day))
print(type(date))
print(type(year))

first_len = len(first_name)
last_len = len(last_name)

print('First name length: ', first_len)
print('Last name length: ', last_len)

num_one = 5
num_two = 4

total = num_one+num_two
diff = num_one-num_two
product = num_one*num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(exp)
print(floor_division)

circle_rad = 30
m_pi = 3.14

area_of_circle = ((circle_rad**2) * m_pi)
circum_of_circle = 2*m_pi*circle_rad

in_rad = int(input('Input your radius to find the area: '))
area_of_circle_in = ((in_rad**2)*m_pi)
print(area_of_circle_in)
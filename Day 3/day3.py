#day 3 - 30 Day challenge: Operators
age = 19
height = 63.5
complx = 3+2j

base = float(input('Enter base: '))
hght = float(input('Enter height: '))
print('The area of a triangel is: ', 0.5*base*hght)

side_a = float(input('Enter side a: '))
side_b = float(input('Enter side b: '))
side_c = float(input('Enter side c: '))
print('The perimeter of the triangle is: ', side_a+side_b+side_c)

i_length = float(input('Enter length: '))
i_width = float(input('Enter width: '))
print('The area is: ', i_length*i_width, ' The perimeter is: ', 2*i_width*i_length)

i_radius = float(input('Enter a radius: '))
m_pi = 3.14
print('The area is: ', (m_pi*i_radius**2), ' The circumference is: ', (2*m_pi*i_radius))

y_intercept = 2*0 - 2
x_intercept = (0/2) + 1
slope = 2
print('The x intercept is: ', x_intercept, ' The y intercept is: ', y_intercept, ' The slope is: ', slope)

point1 = [2,2]
point2 = [6,10]
slope = (point2[1]-point1[1])/(point2[0]-point1[0])
E_dist = print('Eulcidean distance for (2,2), (6,10): ',(((point2[1]-point1[1])**2)+((point2[1]-point1[1])**2)) ** 0.5)

#will print false
str_python = 'python'
str_dragon = 'dragon'
l_python = len(str_python)
l_dragon = len(str_dragon)
print(l_python>l_dragon)
print('Is on in python: ', str_python and 'on')
print('Is on in dragon: ', str_dragon and 'on')

str_jargon = 'I hope this course is not full of jargon'
print('jargon' in str_jargon)

t_num = 10
print('This will be true if a number is even: ', (t_num % 2) ==0)

floor_div = 7//3
int_converted = int(2.7)
print('Is the floor div of 7/3 and the converted in of 2.7 equal: ', (floor_div == int_converted))

str_ten = '10'
print(str_ten == 10)

str_int_conversion = int(float('9.8'))
print(str_int_conversion == 10)

i_hours = float(input('Enter hours: '))
i_rate = float(input('Enter rate per hour: '))
print('Your weekly earning is: ', i_hours*i_rate)

i_years = int(input('Enter number of years you have lived: '))
seconds_lived = i_years*365.25*24*60*60
print('You have lived: ', seconds_lived, ' seconds')

m_table1 = [1,1,1,1,1]
m_table2 = [2,1,2,4,8]
m_table3 = [3,1,3,9,27]
m_table4 = [4,1,4,16,64]
m_table5 = [5,1,5,25,125]
print(m_table1)
print(m_table2)
print(m_table3)
print(m_table4)
print(m_table5)
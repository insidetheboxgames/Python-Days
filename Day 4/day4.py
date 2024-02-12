#day 4 - 30 Day challenge: Strings
str1 = 'Thirty'
str2 = 'Days'
str3 = 'Of'
str4 = 'Python'
space = ' '
full_str = str1+space+str2+space+str3+space+str4
print(full_str)
str1 = 'Coding'
str2 = 'For'
str3 = 'All'
full_str = str1+space+str2+space+str3
print(full_str)
company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
t_company = company[6:]
print(t_company)
print(company)
#index should be 0
print(company.find('Coding'))
company = company.replace('Coding','Python')
print(company)
split_str = company.split(' ')
print(split_str)
list_companies = 'Facebook,Google,Microsoft,Apple,IBM,Oracle,Amazon'
split_list = list_companies.split(',')
print(split_list)

str_main = 'Python For All'
print(str_main[len(str_main)-1])
print(str_main[10])
split_main = str_main.split(' ')
main_acronymn1 = split_main[0][0]
main_acronymn2 = split_main[1][0]
main_acronymn3 = split_main[2][0]
main_acronymn = main_acronymn1+main_acronymn2+main_acronymn3
print(main_acronymn)

str_main = 'Coding For All'
print(str_main[len(str_main)-1])
split_main = str_main.split(' ')
main_acronymn1 = split_main[0][0]
main_acronymn2 = split_main[1][0]
main_acronymn3 = split_main[2][0]
main_acronymn = main_acronymn1+main_acronymn2+main_acronymn3
print(main_acronymn)

print('location of C in Coding For All ',str_main.find('C'))
print('location of C in Coding For All ',str_main.find('F'))
str_main = str_main+' People'
print('location of C in Coding For All People ',str_main.rfind('l'))

str_location = 'You cannot end a sentence with because because because is a conjunction'
print(str_location.index('because'))
str_location = 'You cannot end a sentence with because because because because is a conjunction'
print(str_location.rfind('because'))

str_location = 'You cannot end a sentence with because because because is a conjunction'
str_location1 = str_location[:str_location.index('because because because')]
str_location1 = str_location1 + str_location[str_location.rfind('because')+len('because'):len(str_location)]
print(str_location1)
print(str_location.index('because'))

str_main = 'Coding For All'
print(str_main.find('Coding'))
print(str_main.find('coding'))
str_main = ' Coding For All '
print(str_main)
str_main = str_main[1:len(str_main)-1]
print(str_main)

str_m = '30DaysOfPython'
print(str_m.isidentifier())
str_m = 'thirty_days_of_python'
print(str_m.isidentifier())

name_list =  ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
name_hash =  ' '.join(name_list)
print(name_hash)
print('I am enjoying this challenge \nI just wonder what is next.')

print('Name\tAge\tCountry\tCity\nname\t19\tUS\tD.C.')

str_1 = 'radius = 10 \narea = 3.14 * radius ** 2\nThe area of a circle with radius 10 is 314 meters square.'
print(str_1)
str_formatted = '8 + 6 = 14\n8 - 6 = 2\n8 * 6 = 48\n8 / 6 = 1.33\n8 % 6 = 2\n8 // 6 = 1\n8 ** 6 = 262144'
print(str_formatted)
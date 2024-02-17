#day 9 - 30 Day challenge: Conditionals
in_age = int(input("Enter your age: "))
if in_age >= 16:
    print("You are old enough to learn to drive.")
else:
    print("You need ", 16-in_age," more years to learn to drive.")

my_age = 19

if in_age > my_age:
    print("You are ", in_age-my_age," years older than me.")
elif in_age < my_age:
    print("You are ", my_age - in_age, " years younger than me.")
else:
    print("We are the same age")

in_num1 = int(input("Enter number one: "))
in_num2 = int(input("Enter number two: "))

if in_num1 > in_num2:
    print(in_num1, " is greator than ",in_num2)
elif in_num1 < in_num2:
    print(in_num2, " is greator than ",in_num1)
else:
    print(in_num1, " is equal to ", in_num2)

stud_score = int(input("Enter a students score 0-100: "))
#I want this grading style
if stud_score >= 80:
    print("Grade is an A")
elif stud_score >= 70:
    print("Grade is a B")
elif stud_score >= 60:
    print("Grade is a C")
elif stud_score >= 50:
    print("Grade is a D")
else:
    print("Grade is a F")

autumn = ['September','October','November']
winter = ['December','January','February']
spring = ['March','April','May']
summer = ['June','July','August']

in_season = input("Enter the month")
in_season.capitalize()
print(type(in_season))
print(in_season)

if in_season in autumn:
    print("The season for ", in_season, " is Autumn")
elif in_season in winter:
    print("The season for ", in_season, " is Winter")
elif in_season in spring:
    print("The season for ", in_season, " is Spring")
elif in_season in summer:
    print("The season for ", in_season, " is Summer")
else:
    print("The season for ", in_season, " Does not exists. It is not a valid month")

fruits = ['banana', 'orange', 'mango', 'lemon']
in_fruit = input("Enter a fruit: ")
in_fruit.lower()
if in_fruit in fruits:
    print("That fruit already exists in the list")
else:
    fruits.append(in_fruit)

m_person = {
    'first_name': 'Aidan',
    'last_name': 'C',
    'age': 19,
    'country': 'USA',
    'is_marred': False,
    'skills': ['C++', 'Verilog', 'ASM', 'C', 'Discrete Math'],
    'address': {
        'street': 'NOPE',
        'zipcode': '00000'
    }
}

person_keys = list(m_person.keys())

if 'skills' in person_keys:
    t_skills = m_person.get('skills')
    print(t_skills[len(t_skills)//2])
if 'skills' in person_keys:
    t_skills = m_person.get('skills')
    if 'Python' in t_skills:
        print("The person has Python in their skills")
    else:
        print("The person does not have Python in their skills")
else:
    print("The person does not have skills in their data")

if 'skills' in person_keys:
    t_skills = m_person.get('skills')
    if 'C++' in t_skills:
        if 'ASM' in t_skills:
            print("They are a low level programmer")
        elif 'Discrete Math':
            print("They are a college programmer")
    else:
        print("Not enough Data to determine type of programmer")

if m_person['is_marred'] == False:
    if m_person['country'] == 'USA':
        print(m_person['first_name'], " lives in ", m_person['country'],". He is not married.")
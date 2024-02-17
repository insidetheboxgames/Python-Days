#day 8 - 30 Day challenge: Dictionaries
#very messy terminal today
dog = {}
print(dog)
dog['Name'] = 'Frodo'
dog['Color'] = 'Golden'
dog['breed'] = 'Doodle'
dog['legs'] = 4
dog['age'] = 5
print(dog)
student = {'first_name':'Aidan','last_name':'C','gender':'M','age':19,'marital_status':False,'skills':['C++','Verilog','ASM','Python'],'country':'USA','city':'Pullman','address':'NOPE'}

print(student)
print(len(student))
skills = student.get('skills')
print(type(skills))
student['skills'].append('Discrete Math')
print(student)

list_of_dict_keys = list(student.keys())
print(list_of_dict_keys)
print(type(list_of_dict_keys))

list_of_dict_vals = list(student.values())
print(list_of_dict_vals)
print(type(list_of_dict_vals))

student_tuple = student.items()
print(student_tuple)

student.pop('marital_status')
print(student)
del student
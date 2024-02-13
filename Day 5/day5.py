#day 4 - 30 Day challenge: Lists
empty_lst = list()
five_var_lst = ['Banana','Orange','Lemon','Strawberry','Peach']
print(len(five_var_lst))
middle = len(five_var_lst)//2
print('The first element is: ', five_var_lst[0],' The middle element is: ', five_var_lst[middle], ' The last element is: ', five_var_lst[len(five_var_lst)-1])
mixed_data_types = ['Name', 19, 63.5, False, 'Address']
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(it_companies)
print('The number of companies is: ',len(it_companies))
middle_comp = len(it_companies)//2
print('The first element is: ', it_companies[0],' The middle element is: ', it_companies[middle_comp], ' The last element is: ', it_companies[len(it_companies)-1])
it_companies[5] = 'NVIDIA'
print(it_companies)
it_companies.insert(1,'AMD')
print(it_companies)
it_companies.insert((len(it_companies)//2),'Intel')
print(it_companies)
it_companies[2] = it_companies[2].capitalize()
print(it_companies)
str1 = '#; '
it_companies.extend(str1)
print(it_companies)
ind = it_companies.index('IBM')
print(ind)
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
first_three_comp = it_companies[0:3]
last_three_comp = it_companies[len(it_companies)-3:]
print(first_three_comp)
print(last_three_comp)
print(it_companies)
middle_comp_ind = len(it_companies)//2
middle_comp_str = it_companies[middle_comp_ind]
print(middle_comp_str)
del it_companies[0]
middle_comp_ind = len(it_companies)//2
del it_companies[0:]
it_companies.clear();
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joint_lst = front_end+back_end
print(joint_lst)
full_stack = joint_lst
full_stack.insert(full_stack.index('Redux')+1, 'Python')
full_stack.insert(full_stack.index('Python')+1, 'SQL')
print(full_stack)

ages = [19,22,19,24,20,25,26,24,25,24]
ages.sort()
print('Min age is: ', ages[0], ' Max age is: ', ages[len(ages)-1])
ages.insert(0, ages[0])
ages.insert(len(ages)-1, ages[len(ages)-1])
print(ages)
ages_mid = len(ages)//2
ages_median = ages[ages_mid]
print(ages_median)
summation=0
for i in ages:
    summation += i

summation/=len(ages)
print(summation)
age_range = ages[len(ages)-1] - ages[0]
print(age_range)
print('min - ave: ', abs(ages[0]-summation),' max-ave: ', abs(ages[len(ages)-1]-summation))

#Countries exercise
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];
countries_size = len(countries)
list1 = list()
list2 = list()
if(countries_size %2 == 0):
    list1 = countries[0:countries_size/2]
    list2 = countries[(countries_size/2)+1:]
else:
    list1 = countries[0:countries_size//2]
    list2 = countries[(countries_size//2)+1 :]

print(list1)
print(list2)
countries_two = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
countries_unpacked1,countries_unpacked2,countries_unpacked3, *countries_scandic = countries_two
countries_unpacked = list()
countries_unpacked = countries_unpacked1+countries_unpacked2+countries_unpacked3
print(countries_unpacked)
print(countries_scandic)
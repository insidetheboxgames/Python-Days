#day 11 - 30 Day challenge: Functions

def add_two_numbers(a, b):
    return a+b
print(add_two_numbers(5,5))

def area_of_circle(radius):
    return 3.14*radius*radius
print(area_of_circle(2))

def add_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(add_all_nums(10,15,12,31,51,31,1))

def celsius_to_fahrenheit(celsius):
    return (celsius*(1.8))+32
print(celsius_to_fahrenheit(10))

def check_season(month):
    autumn = ['September','October','November']
    winter = ['December','January','February']
    spring = ['March','April','May']
    summer = ['June','July','August']
    #makes sure it is a string
    #Horribly unoptimized
    month = str(month)
    month.capitalize()
    if month in autumn:
        return "Autumn"
    elif month in winter:
        return "Winter"
    elif month in spring:
        return "Spring"
    elif month in summer:
        return "Summer"
    else:
        return "Input was not a valid month"
print(check_season("April"))

def calc_slope(x1,x2,y1,y2):
    t_slope = (y2-y1)/(x2-x1)
    return t_slope
print(calc_slope(2,3,10,15))

def solve_quadratic_eqn(a,b,c):
    sol_set =list()
    x = ((-b)+((b**2)-(4*a*c))**(1/2))/(2*a)
    sol_set.append(x)
    x = ((-b)-((b**2)-(4*a*c))**(1/2))/(2*a)
    sol_set.append(x)
    return sol_set
print(solve_quadratic_eqn(1,8,16))

def print_list(lst):
   for i in range(len(lst)):
    print(lst[i])
it_list = ['Python', 'Numpy','Pandas','Django', 'Flask']
print_list(it_list)

#Not my favorite method but works
def reverse_list(lst):
    t_list = list()
    list_len = len(lst)
    for i in range(list_len):
        t_list.append(lst[list_len-i-1])
    return t_list
print(reverse_list([1,2,3,4,5]))
print(reverse_list(["A","B","C"]))

def capitalize_list_items(lst):
    t_list = list()
    for i in range(len(lst)):
        #May not be a string input
        t_item = str(lst[i])
        t_item.capitalize()
        t_list.append(t_item)
    return t_list
print(capitalize_list_items(['python', 'Numpy','pandas','Django', 'flask']))

def add_item(lst, item):
    #I'm making the assumption that lst will be a list
    #See capitalize_list_items for what I would do if I wasn't making that assumption
    lst.append(item)
    return lst
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat'))    
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))

def remove_item(lst, item):
    #I'm making the assumption that lst will be a list
    #See capitalize_list_items for what I would do if I wasn't making that assumption
    #Also that item is in the list
    lst.remove(item)
    return lst
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango')) 
numbers = [2, 3, 7, 9];
print(remove_item(numbers, 3))

def sum_of_all_nums(num):
    sum = 0
    for i in range(num,0,-1):
        sum += i
    return sum
print(sum_of_all_nums(5))  
print(sum_of_all_nums(10)) 
print(sum_of_all_nums(100))

def sum_of_odds(num):
    sum = 0
    for i in range(num, 0, -1):
        if i%2 != 0:
            sum += i
    return sum
print(sum_of_odds(5))  
print(sum_of_odds(10)) 
print(sum_of_odds(100))
def sum_of_evens(num):
    sum = 0
    for i in range(num, 0, -1):
        if i%2 == 0:
            sum += i
    return sum
print(sum_of_evens(5))  
print(sum_of_evens(10)) 
print(sum_of_evens(100))

def even_and_odds(num):
    evens = 0
    odds = 0
    for i in range(num,-1,-1):
        if i %2 ==0:
            evens += 1
        else:
            odds += 1
    res = list()
    res.append("There are "+str(evens)+" evens")
    res.append("There are "+str(odds)+" odds")
    return res
print(even_and_odds(100))

def calc_factorial(num):
    result = 1
    for i in range(1,num+1,1):
        result *= i
    return result
print(calc_factorial(5))

def is_empty(lst):
    if not lst:
        return True
    else:
        return False
print(is_empty([]))
print(is_empty(['Potato', 'Tomato', 'Mango', 'Milk']))

def calc_mean(nums):
    res = 0
    length = len(nums)
    for i in nums:
        res += i
    return res/length
print(calc_mean([2, 3,5,6, 7, 9,10]))

def calc_median(nums):
    lst_len_f = len(nums)%2
    lst_len_c = ((len(nums)-1) // 2)+1
    res = 0.0
    if lst_len_f == 0:
        res = (nums[lst_len_c-1] + nums[lst_len_c])/2
    else:
        res = nums[lst_len_c-1]
    return res
print(calc_median([2, 3,5,6, 7, 9,10]))

def calc_range(nums):
    nums.sort()
    res = list()
    res.append(nums[0])
    res.append(nums[len(nums)-1])
    return res
print(calc_range([2, 3,5,6, 7, 9,10]))

def calc_variance(nums):
    sum = 0
    mean = calc_mean(nums)
    total_entries = len(nums)
    for i in nums:
        sum += (i - mean)**2
    return (sum/total_entries)
print(calc_variance([2, 3,5,6, 7, 9,10]))

#can also be calc_variance(nums)**(0.5)
def calc_std(nums):
    sum = 0
    mean = calc_mean(nums)
    total_entries = len(nums)
    for i in nums:
        sum += (i - mean)**2
    return (sum/total_entries)**(0.5)
print(calc_std([2, 3,5,6, 7, 9,10]))

def is_prime(num):
    for i in range(2,int(num**(1/2))+1):
        if(num % i) == 0:
            return False
    return True
print(is_prime(13))
print(is_prime(22))

def is_unique(lst):
    t_lst = list()
    for i in lst:
        for j in t_lst:
            if i == j:
                return False
        t_lst.append(i)
    return True
print(is_unique(['Potato', 'Tomato', 'Mango', 'Milk']))
print(is_unique(['Potato', 'Tomato', 'Mango', 'Milk', 'Tomato']))
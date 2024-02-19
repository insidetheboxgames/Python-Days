#day 12 - 30 Day challenge: Modules
from random import random, randint
import string

def random_user_id():
    randID = ""
    allCharStr = string.ascii_letters+string.digits
    indexLength = len(allCharStr)
    for i in range(6):
        rand_chr = randint(0,indexLength-1)
        randID = randID+allCharStr[rand_chr]
    return randID
print(random_user_id())

def user_id_gen_by_user():
    id_length = int(input("How many character would you like your randID to be: "))
    ids = int(input("How many IDS would you like: "))
    randID = list()
    #Could just hard code this number
    allCharStr = string.ascii_letters+string.digits
    indexLength = len(allCharStr)
    for i in range(ids):
        t_res = ""
        for j in range(id_length):
            rand_chr = randint(0, indexLength-1)
            t_res = t_res+allCharStr[rand_chr]
        randID.append(t_res)
    return randID
print(user_id_gen_by_user())

def rand_rgb_gen():
    rgb_colors = list()
    for i in range(3):
        rgb_colors.append(randint(0,255))
    return rgb_colors
print(rand_rgb_gen())

def list_of_hex_colors():
    num_Colors = int(input("How many hex colors could you like to be generated: "))
    hexChars = "0123456789abcdef"
    lst_colors = list()
    for i in range(num_Colors):
        color_str = "#"
        for j in range(6):
            rand_chr = randint(0,15)
            color_str += hexChars[rand_chr]
        lst_colors.append(color_str)
    return lst_colors
print(list_of_hex_colors())

def list_of_rgb_colors():
    num_Colors = int(input("How many rgb colors could you like to be generated: "))
    lst_colors = list()
    for i in range(num_Colors):
        rgb_lst = list()
        for j in range(3):
            rand_chr = randint(0,255)
            rgb_lst.append(rand_chr)
        lst_colors.append(rgb_lst)
    return lst_colors
print(list_of_rgb_colors())

def generate_colors(color_type, number_of_colors):
    lst_colors = list()
    if color_type == 'hexa':
        hexChars = "0123456789abcdef"
        for i in range(number_of_colors):
            color_str = "#"
            for j in range(6):
                rand_chr = randint(0,15)
                color_str += hexChars[rand_chr]
            lst_colors.append(color_str)
        return lst_colors
    elif color_type == 'rgb':
        for i in range(number_of_colors):
            rgb_lst = list()
            for j in range(3):
                rand_chr = randint(0,255)
                rgb_lst.append(rand_chr)
            lst_colors.append(rgb_lst)
        return lst_colors
    else:
        print(color_type," Is not a supported color type, Either hexa or rgb is supported")
        return
print(generate_colors('hexa', 3))
print(generate_colors('hexa', 1))
print(generate_colors('rgb', 3)) 
print(generate_colors('rgb', 1))

def shuffle_list(lst):
    lst_len = len(lst)-1
    for i in range(lst_len):
        rand_index1 = randint(0,lst_len)
        rand_index2 = randint(0,lst_len)
        t_item = lst[rand_index1]
        lst[rand_index1] = lst[rand_index2] 
        lst[rand_index2] = t_item
    return lst
print(shuffle_list(['C++', 'Verilog', 'ASM', 'C', 'Discrete Math']))

def rand_seven_num_zero_nine():
    num_lst = list()
    num_lst.append(randint(0,9))
    duplicate_flag = False
    while len(num_lst) != 7:
        rand_num = randint(0,9)
        for i in range(len(num_lst)):
            if rand_num == num_lst[i]:
                duplicate_flag = True
        if duplicate_flag == False:
            num_lst.append(rand_num)
        duplicate_flag = False
    return num_lst
print(rand_seven_num_zero_nine())

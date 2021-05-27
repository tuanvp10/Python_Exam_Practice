# The dictionary that will be passed is as below:

# shopping_items = {"eggs": 5.85, "bread": 3.50, "ice": 0.30}

# create a function called calculate_total_basket_cost(shoppingList):

# calculate total cost of shopping items

# You must return the total amount only

# def calculate_total_basket_cost(shopping_list):
#
#     sum = 0
#     for items in shopping_items.values():
#         sum = sum + items
#     return sum
#
# shopping_items = {
#     "eggs": 5.85, "bread": 3.50, "ice": 0.30
# }
# print(calculate_total_basket_cost(shopping_items))
#
# # declare a function called with correct syntax called user_name
# def user_name():
#     pass

# how can you iterate over this list_num = [9, ,8 , 7, 6, 5]
# list_num = [9, 8, 7, 6, 5]
#
# x = range(len(list_num))
# print(x)

# Iterate through list in Python using a for Loop
# list_num = [9, 8, 7, 6, 5]
# for x in list_num:
#     print(x)

# Iterate through list in Python with a while loop
# list_num = [9, 8, 7, 6, 5]
# x = 0
# while x < len(list_num):
#     print(list_num[x])
#     x = x + 1

# What is the data collection type for num_id: num_id = {'0':1, '5':9 }
# num_id = {'0':1, '5':9 }
# print(type(num_id))

# Add 9 to the list:
# value_list = [9, 8, 7, 6, 5]
# value_list.append(9)
# print(value_list)

# Create a function called greetings that takes 1 string arg "name", should return True if arg is equal to string "name" False otherwise

# def greetings(name):
#     if name == "name":
#         return True
#     else:
#         return False
# name = "hello"
# print(greetings(name))

# Declare a function that takes a list of numbers as an arg, should iterate over the list and return only even numbers from the list, create a list with numbers 1 to 11 to use in this function

# def even_numbers(list):
#     evens = []
#     for x in list:
#         if x % 2 == 0:
#             evens.append(x)
#     return evens
#
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# print(even_numbers(list))

# Create a basic calculator with add, subtract, divide and multiply with return statements to return the mathematical value

# def calculate():
#     operation = input('''Please type in the math operation you would like to complete:
# + for addition
# - for subtraction
# * for multiplication
# / for division
# ''')
#
#     number_1 = int(input('Please enter the first number: '))
#     number_2 = int(input('Please enter the second number: '))
#
#     if operation == '+':
#         print('{} + {} = '.format(number_1, number_2))
#         print(number_1 + number_2)
#
#     elif operation == '-':
#         print('{} - {} = '.format(number_1, number_2))
#         print(number_1 - number_2)
#
#     elif operation == '*':
#         print('{} * {} = '.format(number_1, number_2))
#         print(number_1 * number_2)
#
#     elif operation == '/':
#         print('{} / {} = '.format(number_1, number_2))
#         print(number_1 / number_2)
#
#     else:
#         print('You have not typed a valid operator, please run the program again.')
#
# # Call calculate() outside of the function
# calculate()

def calculate():
    operation = input('''Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division \n
''')

    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))

    if operation == '+':
        print(number_1 + number_2)

    elif operation == '-':
        print(number_1 - number_2)

    elif operation == '*':
        print(number_1 * number_2)

    elif operation == '/':
        print(number_1 / number_2)

    else:
        print('You have not typed a valid operator, please run the program again.')

# Call calculate() outside of the function
calculate()
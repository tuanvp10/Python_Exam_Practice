# Python Practice Exam Questions

### The dictionary that will be passed is as below:
shopping_items = {"eggs": 5.85, "bread": 3.50, "ice": 0.30}
- create a function called calculate_total_basket_cost(shoppingList):
- calculate total cost of shopping items
- You must return the total amount only

```python
def calculate_total_basket_cost(shopping_list):

    sum = 0
    for items in shopping_items.values():
        sum = sum + items
    return sum

shopping_items = {
    "eggs": 5.85, "bread": 3.50, "ice": 0.30
}
print(calculate_total_basket_cost(shopping_items))
```

### Declare a function called with correct syntax called user_name

```python
def user_name():
    pass
```

### How can you iterate over this list_num = [9, ,8 , 7, 6, 5]

#### There are so many ways to iterate through this list. 

- Using the `range()` method, which could be used in combination with a for loop to traverse and iterate over this list. 
  - This method basically returns sequence of integers i.e. it builds/generates a sequence of integers from the provided start index up to the end index as specified in the argument list.
  - Syntax:

    range (start, stop[, step])
    - start: Optional. An integer number specifying at which position to start. Default is 0
    - stop Required. An integer number specifying at which position to stop (not included).
    - step	Optional. An integer number specifying the incrementation. Default is 1
    
```python
list_num = [9, 8, 7, 6, 5]

x = range(len(list_num))
print(x)

# output = range(0, 5)
```

- Iterate through list in Python using a for Loop
```python
list_num = [9, 8, 7, 6, 5]
for x in list_num:
    print(x)
```
- Iterate through list in Python with a while loop
  - Python while loop can also be used to iterate the list in similar fashion as that of for loops.
  
```python
list_num = [9, 8, 7, 6, 5]
x = 0
while x < len(list_num):
    print(list_num[x])
    x = x + 1
```
### How would you apply an and operation between 2 boolean values

- The and operator takes two arguments. It evaluates to False unless both inputs are True. 

### Difference between list and tuple

- The main difference between lists and tuples is the fact that lists are mutable whereas tuples are immutable.

- A mutable data type means that a python object of this type can be modified.

- An immutable object can’t.

### Can you add items to tuple?

- The answer is no.

### What is the data collection type for num_id: num_id = {'0':1, '5':9 }

- <class 'dict'>
```python
num_id = {'0':1, '5':9 }
print(type(num_id))

```

### What is the syntax to create an object of a class?

```python
# Creating a class
class MyClass():
    x = 5
# Creating an object of a class, object named p1, and print the value of x:
p1 = MyClass()
print(p1.x)
```

### Adding to a list, value_list = [9, 8, 7, 6, 5], add 9 to this list

```python
value_list = [9, 8, 7, 6, 5]
value_list.append(9)
print(value_list)

```

### Create a function called greetings that takes 1 string arg "name", should return True, if arg is equal to string "name" False otherwise

```python
def greetings(name):
    if name == "name":
        return True
    else:
        return False
name = "hello"
print(greetings(name))
```

### Write the syntax to inherit class A in class B

```python
# Two classes = class A and class B
from A import B
```

### Write the syntax for super
```python
from A import B

class B(A):
  
  def __init__(self):
    super().__init()
```

### Declare a function that takes a list of numbers as an arg, should iterate over the list and return only even numbers from the list, create a list with numbers 1 to 11 to use in this function

```python
def even_numbers(list):
    evens = []
    for x in list:
        if x % 2 == 0:
            evens.append(x)
    return evens

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(even_numbers(list))
```

### Create a basic calculator with add, subtract, divide and multiply with return statements to return the mathematical value

```python
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
```

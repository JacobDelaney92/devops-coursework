age = 20
price = 19.95
first_name = 'Jacob'
is_online = False
print(age)

# create a patient check in form
patient = 'Jacob Delaney'
age = 29
new_Patient = True

# creating input
#name = input('what is your name?')
#print('hello' + name)

# Type Conversion
#birth_year = input('Enter your birth here')
#age = 2022 - int(birth_year)
#print(age)
# int = 20
# float = 20.1
#int()
#float()
#bool()
#str()
#first = input("First:")
#second = input("Second:")
#sum = int(first) + int(second)
#print(sum)
course = 'python for beginners'
#print(course.upper())
#print(course.lower())
#checking to see if python is in course variable
print('python' in course)

#Arithmetic operators 
print(10/3)#float
print(10//3)#interger
print(10%3)#interger
print(10**3)#interger


#Exercises
some_prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
print(some_prime_numbers[9])

#Dictionary
#Exercise 3.5
eggs = { 'name': 'Free Range Large Eggs', 'individual_price': 1.89, 'number': 2 }
print(eggs['individual_price'] *  eggs['number'])
#Exercise 3.6
# Put two guests in room 101, no guests in room 102, and one guest in room 201.
hotel = {'room 101':['John Smith','Daniel books'],'room 102':[],'room 201':['Alan Stubs'],}
print(hotel)
#Exercise 3.7
print(hotel['room 101'])
print(len(hotel['room 201']))
print(bool(hotel['room 102']))
#Exercise 3.8
user = { 'name': 'Jamie', 'age': 41, 'address': { 'postcode': 'W2 3AN', 'first_line': '23 Leinster Gardens' } }
#Write an expression to get the user’s address (the nested dictionary).
#Write an expression to get just the user’s postcode (just a single string).
print(user['address'])
print(user['address']['postcode'])

#Exercise 3.9
#The final command here is throwing an error:
budget = 12.50
expenditure = 4.25 + 5.99
print(expenditure < budget)
#Exercise 3.10
#What is wrong with the following block of code? Can you fix the mistake?

my_string = 'Hello, world'
my_dictionary = { 'greeting': my_string, 'farewell': 'Goodbye, world' }
print(my_dictionary)

#Exercise 3.11
#Why does this produce an error instead of the string ‘Alice’? Can you fix the mistake?

user_by_id = { '159': 'Alice', '19B': 'Bob' }
print(user_by_id['159'])

#Shopping Cart
#Exercise
#We have a list of items in a shopping cart.
#  We want to find out the total cost, but it’s quite complicated.
#  We need to write a Python script to calculate the cost for us!

#We have a shopping cart with:

shopping_cart = [{'name': 'apple', 'price_per_item': 0.21, 'number': 4}, {'name': 'banana', 'price_per_item': 0.12, 'number': 5}]

apple_total = float(shopping_cart[0]['price_per_item']) * float(shopping_cart[0]['number'])
banna_total = float(shopping_cart[1]['price_per_item']) * float(shopping_cart[1]['number'])
apple_discount = apple_total / 2

#together
before_sale_tax = '£' + str(apple_total + banna_total)
after_sale = '£' + str(apple_discount + banna_total)
total_sale_tax = (apple_discount + banna_total) * 1.15

#output
print('Cost of basket before sales and tax: ' + before_sale_tax)
print('Cost of basket after sales, before tax: ' + after_sale)
print((f"Cost of basket after sales and tax: £ {total_sale_tax:.2f}"))

# Function Lists
print('hello')
def add_func(x,y):
    return x + y
print(add_func(3,4))

#Dictonary
def get_age(person):
    return person['age']

bob = {
    "name": "Bob",
    "age": 50,
    "starsign": "Taurus"
}
print(get_age(bob))

# cannot change a value 
var1 = 4
#var2 = var1
#var1.append(3)
dir([1]) # list all the methods
print(dir([1]))
print(var1)
s = 'hello'
print(s[0])
l = ['h','e','l','l']
print(l[2])

#if statement 
if True: 
    print('HI')
#python defines code with white space so indentend code like above is fine  

print(len(s))

for el in l:
    print(el)

def myFunction(value):
    return print(value + ' ya mum')
myFunction('haha')

def many(a,b,c):
    return print(a + b + c)
many(4,8,9)

def passing(a,b):
    return print(a + b)

passing(5,8)

#adding to an object
d = {
    'monkey':'chimp'
}    
d['cat'] = 'tiger'    

print(d)

def calc(a,b,c):
    return print(a,b,c)
calc(1,2,3)

results = []
#get file 
f = open('calcFile.txt', mode='r')
#open file
with open('calcFile.txt', 'r') as f:
    #split file into an array
    text_string = f.read().splitlines()
    #loop through the array
    for x in text_string:
        #split the array
        values = x.split()
        #pass through the values from the array
        def calculator(operator, value1, value2):
            if(operator == "x"):
               times = int(value1) * int(value2)
               timesResults = []
               timesResults.append(times)
               results.append(timesResults)

            if(operator == "-"):
               print(int(value1) - int(value2)) 
            if(operator == "/"):
               print(int(value1) / int(value2)) 
            
        calculator(values[1],values[2],values[3])

print(results)
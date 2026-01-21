'''
x = 10 
print(x) 

x = 23 
print(x)

y = None 
print(y)

y = 2

z = ( x + y)/x + (78%3) 
print(z)

name = "bobby"
nameType = type(name) 
print(nameType)


age = 12
ageType = type(age)
print(ageType) 


height = 6.5
heightType = type(height)
print(heightType) 

hasDate = False
hasDateType = type(hasDate)
print(hasDateType) 

comp = 7j 
compType = type(comp)
print(compType) 

message = f'Hi my name is {name} I am {age} years old'
print(message) 


intHeight = int(height) 
strHeight = str(height) 
floatHeight = float(intHeight) 

name  = input("Enter name: ")
print (name)

if 3 > 5:
  print("more")

else :
 print("less") 


if 3 > 5: print ("more")
else : print ("less")


mark = input("Enter mark: ")
mark = int(mark)

if mark > 70:
  print("A")

elif mark > 60: 
  print("B")

elif mark > 50: 
  print("C")

else:
  print("F") 

i = 1
while i < 10:
 print(i)
 i+=1
else:
 print("This is run when the loop condition is no longer met")


list = ["bob", "sally", "john"]
for j in list:
 print(j)


for i in range(0, 10, 2):
 print(i)


def add(a, b):
    return a + b

def printPerson(name, age, height):
    print(name, age, height)


printPerson(age=12, name='bob', height=5)


def sayHello(fname, lname='Smith'):
    print('Hello '+fname + ' ' + lname)

sayHello('John')

sayHello('Bill', 'Young')


def multiReturnFunc(a,b):
    return a+b, a-b, a*b, a/b


numSum, numDiff, numMult, numDiv = multiReturnFunc(10,5) 
print(numSum, numDiff, numMult, numDiv)


list = ['item1', 'item2', 'item3']
list2 = [12, 33, 45, 58, 23]

print(list)

print(list2[-1])


print(list2[2:4])


print(len(list2))


list.append('item4')


item4 = list.pop()


list3 = list2.copy()



num = [ 1, 2, 3, 4]
doubled = [n*2 for n in num]
print(doubled) 
odd = [ n for n in num if n%2 == 1]
print(odd) 


num = [ 1, 2, 3, 4]
[first, second, *rest] = num
print(first)
print(second)
print(rest)

num2 = [5, 6]
num3 = num + num2
print(num3)

num4 = num2.copy()
'''

from fastapi import FastAPI
import json

app = FastAPI()

global data

with open('./data.json') as f:
    data = json.load(f)

#Task 2: http://localhost:8000/
@app.get('/')
async def hello_world():
    return 'Hello, World!'

#Task 3: http://localhost:8000/students
@app.get('/students')
async def get_students():
    return data

#Task 4: http://localhost:8000/students/STD0001
@app.get('/students/{id}')
async def get_student(id):
  for student in data: 
    if student['id'] == id: 
      return student

#Task 5: http://localhost:8000/students?pref=Chicken
@app.get('/students')
async def get_students(pref: str = None):
    if pref:
        filtered_students = []
        for student in data:
            if student['pref'] == pref:  
                filtered_students.append(student)  
        return filtered_students
    return data

#Exercise 1: http://localhost:8000/stats
@app.get('/stats')
async def get_stats():
    stats = {}
    for student in data:
        # Count meal preference
        pref = student.get('pref')
        if pref:
            stats[pref] = stats.get(pref, 0) + 1

        # Count programme
        programme = student.get('programme')
        if programme:
            stats[programme] = stats.get(programme, 0) + 1

    return stats

#Exercise 2:
#http://localhost:8000/add/5/10
@app.get('/add/{a}/{b}') 
async def add(a: float, b: float):
    result = a + b
    print(result)
    return result

#http://localhost:8000/subtract/5/10
@app.get('/subtract/{a}/{b}')
async def subtract(a: float, b: float):
    result = a - b
    print(result)
    return result

#http://localhost:8000/multiply/5/10
@app.get('/multiply/{a}/{b}')
async def multiply(a: float, b: float):
    result = a * b
    print(result)
    return result

#http://localhost:8000/divide/5/10
@app.get('/divide/{a}/{b}')
async def divide(a: float, b: float):
    if b == 0:
        print("Division by zero")
        return {"error": "Division by zero is not allowed"}
    result = a / b
    print(result)
    return result
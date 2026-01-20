from fastapi import FastAPI
import json

app = FastAPI()

global data

with open('./data.json') as f:
    data = json.load(f)

#Task 2 http://localhost:8000/
@app.get('/')
async def hello_world():
    return 'Hello, World!'

#Task 3 http://localhost:8000/students
@app.get('/students')
async def get_students():
    return data

#Task 4 http://localhost:8000/students/STD0001
@app.get('/students/{id}')
async def get_student(id):
  for student in data: 
    if student['id'] == id: 
      return student

#Task 5 http://localhost:8000/students?pref=Chicken
@app.get('/students')
async def get_students(pref: str = None):
    if pref:
        filtered_students = []
        for student in data:
            if student['pref'] == pref:  
                filtered_students.append(student)  
        return filtered_students
    return data


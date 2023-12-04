
#uvicorn projetctname:app --reload

from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

print('loading...')

student = {
    1 : {
        "name": "Student 1",
        "age": 11,
        "isStudent": True
         },
    2 : {
        "name": "Student 2",
        "age": 21,
         "isStudent": True
        },
    3 : {
        "name": "Student 3",
        "age": 31,
         "isStudent": False
    }
}

class StudentClass(BaseModel):
    name: str
    age: int
    isStudent: bool


app1 = FastAPI()

@app1.get("/")
def home():
    return {"name": "Mukhiddin///", "surname": "Sirojiddinov///"}


@app1.get("/get-all")
def get_all_users():
    return student

@app1.get("/getUser/{id}")
def user(id:int = Path(description= "enter student id ,it will return student info", lt=4, gt=0)):
    return student[id]

@app1.get("/get-by-name")
def get_user_by_name(name: Optional[str] = None):
    for id in student:
        if student[id]["name"] == name:
            return student[id]
    return {"Data":  "not found"}


@app1.post("/add-new-user/{id}")
def add_new_user(id:int,studentobj: StudentClass):
    if id in student:
        return {"error": "id not valid"}
        
    student[id] = studentobj
    return {"Success": True}


@app1.put("/update-user/{id}")
def update_user(id: int, studentobj: StudentClass):
    
    if id not in student:
        return {"error": "user not found"}
    
    student[id] = studentobj
    
    return student[id]
 
 
@app1.delete("/remove-user/{id}")
def remove_user(id: int):
     if id not in student:
    
         return {"error":"user not found"}
     del student[id]
     return {"success": True}
             

print('Done!!!')
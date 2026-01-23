from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


#in-memory employee list
# Employees endpoint
@app.get("/employees")
def get_employees():
    return {"employees":[
        {"id": 1, "name" : "John Doe", "role":"Accountant"},
        {"id": 2, "name" : "Jane Smith", "role":"HR"},
        {"id": 3, "name" : "Emily Johnson", "role":"Manager"}
    ] 
    }

#pydantic model for validation

class Employee(BaseModel):
    id: int
    name: str
    role: str

    # Health endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}


#existing GET endpoint 

@app.get("/employees")
def get_employees():
    return {"employees": employees}
    
#NEW POST endpoint
@app.post("/employees")
def add_employee(employee: Employee):
    employees.append(employee.dict())
    return {"message": "Employee added successfully", "employee": employee}
    
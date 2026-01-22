from fastapi import FastAPI

app = FastAPI()

@app.get("/employees")
def get_employees():
    return {"employees":[
        {"id": 1, "name" : "John Doe", "role":"Accountant"},
        {"id": 2, "name" : "Jane Smith", "role":"HR"},
        {"id": 3, "name" : "Emily Johnson", "role":"Manager"}
    ] 
    }


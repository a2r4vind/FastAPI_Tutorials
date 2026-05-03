from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal 
import json

app = FastAPI()

class Patient(BaseModel):
    
    id: Annotated[str, Field(..., description="The unique identifier for the patient", examples=["P001"])]
    name: Annotated[str, Field(..., description="Name of the patient")]
    age: Annotated[int, Field(..., gt=0, lt=120, description="Age of the patient in years")]
    gender: Annotated[Literal['Male', 'Female', 'Other'], Field(..., description="Gender of the patient")]
    city: Annotated[str, Field(..., description="City where the patient lives")]
    height: Annotated[float, Field(..., gt=0, description="Height of the patient in meters")]
    weight: Annotated[float, Field(..., gt=0, description="Weight of the patient in kilograms")] 

    @computed_field
    @property
    def bmi(self) -> float:
        bmi_value = self.weight / (self.height ** 2)
        return round(bmi_value, 2)
    
    @computed_field
    @property
    def verdict(self) -> str:
        bmi_value = self.bmi
        if bmi_value < 18.5:
            return "Underweight"
        elif 18.5 <= bmi_value < 25:
            return "Normal"
        elif 25 <= bmi_value < 30:
            return "Overweight"
        else:
            return "Obese"

# helper function
def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)

    return data

def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f)

@app.get("/")
# def hello():
#     return {'message': 'Hello, world!'}
def hello():
    return {'message': "Patient management System API"}

@app.get("/about")
# def about():
#     return {'message': 'I am Arvind Kumar Verma and I like to learn new things because I enjoy learning process.'}
def about():
    return {'message': "Fully functional API that manages Patients records"}

@app.get('/view')
def view():
    data = load_data()

    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description="The ID of the patient to retrieve from DB", example="P001")):
    # load all the patients data
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description="Sort on the basis of height or weight"), order: str = Query('asc', description="sort in asc or desc order")):

    valid_fields = ['height', 'weight']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid field, select from {valid_fields}")
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid order, select from 'asc' or 'desc'")
    
    data = load_data()

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=(order == 'desc'))

    return sorted_data

@app.post('/create')
def create_patient(patient: Patient):

    # load existing data
    data = load_data()

    # check if patient with same id already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient with this ID already exists")

    # add new patient to database(json file)
    data[patient.id] = patient.model_dump(exclude=['id'])

    # save data back to json file
    save_data(data)

    # json response that new patient has been created successfully 
    return JSONResponse(status_code=201, content={"message": "Patient created successfully"})

    
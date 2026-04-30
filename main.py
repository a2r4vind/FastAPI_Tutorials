from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

# helper function
def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)

    return data

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
    
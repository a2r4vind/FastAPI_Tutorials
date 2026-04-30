from fastapi import FastAPI
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
    return {'message': "Patient management System"}

@app.get("/about")
# def about():
#     return {'message': 'I am Arvind Kumar Verma and I like to learn new things because I enjoy learning process.'}
def about():
    return {'message': "Fully functional API that manages Patients records"}

@app.get('/view')
def view():
    data = load_data()

    return data
from pydantic import BaseModel

class Patient(BaseModel):

    name: str
    age: int

def insert_patient_data(patient: Patient):
    # simulate inserting patient data into a database
    print(patient.name)
    print(patient.age)
    print("Patient data inserted successfully.")

def update_patient_data(patient: Patient):
    # simulate updating patient data into a database
    print(patient.name)
    print(patient.age)
    print("Patient data updated successfully.")

patient_info = {'name': 'John Doe', 'age': 30}
patient1 = Patient(**patient_info)

#insert_patient_data(patient1)

update_patient_data(patient1)
from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class Patient(BaseModel):

    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str]
    email: EmailStr
    contact: Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact:
            raise ValueError('Emergency contact is required for patients above 60 years old')
        return model


def update_patient_data(patient: Patient):
    # simulate updating patient data into a database
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.email)
    print(patient.contact)
    print("Patient data updated successfully.")

patient_info = {'name': 'john doe', 'age': '70', 'weight': 70.5, 'married': False, 'allergies':['peanuts'], 'email': 'john@icici.com',  'contact': {'phone': '1234556789', 'emergency': '9876543210'}}

patient1 = Patient(**patient_info) 

update_patient_data(patient1)
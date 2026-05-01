from pydantic import BaseModel, EmailStr, AnyUrl
from typing import List, Dict, Optional

class Patient(BaseModel):

    name: str
    age: int
    weight: float
    married: bool = False # default value
    allergies: Optional[List[str]] = None  # two way validation
    email: EmailStr
    contact: Dict[str, str]
    linkedin_url: AnyUrl

def insert_patient_data(patient: Patient):
    # simulate inserting patient data into a database
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.email)
    print(patient.contact)
    print(patient.linkedin_url)
    print("Patient data inserted successfully.")

def update_patient_data(patient: Patient):
    # simulate updating patient data into a database
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.email)
    print(patient.contact)
    print(patient.linkedin_url)
    print("Patient data updated successfully.")

patient_info = {'name': 'John Doe', 'age': 30, 'weight': 70.5, 'married': False, 'email': 'john@gmail.com',  'contact': {'phone': '1234556789'}, 'linkedin_url': 'https://www.linkedin.com/in/johndoe/'}
patient1 = Patient(**patient_info)

insert_patient_data(patient1)

# update_patient_data(patient1)
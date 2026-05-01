from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, min_length=2, title="Name of the patient", description="Provides the name of the patient in less than 50 characters and more than 2 characters", examples=["John Doe", "Jane Smith"])] 
    age: int = Field(gt=0, lt=120) # greater than 0 and less than 120
    weight: Annotated[float, Field(gt=0, strict=True)] # greater than 0, prevent type coercion using strict parameter
    married: Annotated[bool, Field(default=False, title="Marital Status", description="Is the patient married or not")] # default value
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]  # two way validation
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
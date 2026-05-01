from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    age: int
    weight: float
    married: bool
    allergies: Optional[List[str]]
    email: EmailStr
    contact: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['hdfc.com', 'icici.com']
        # abc@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid email')
        
        return value
    
    @field_validator('name')
    @classmethod
    def capitalize_name(cls, value):
        return value.title()
    
    @field_validator('age')
    @classmethod
    def validate_age(cls, value, mode='after'):
        if 0 < value < 100:
            return value
        raise ValueError('Age must be in between 0 and 100')
    
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

patient_info = {'name': 'john doe', 'age': '30', 'weight': 70.5, 'married': False, 'allergies':['peanuts'], 'email': 'john@icici.com',  'contact': {'phone': '1234556789'}}

patient1 = Patient(**patient_info) # when mode='after' in field_validator: type coercion -> validation and when mode='before' in field_validator: validation -> type coercion

update_patient_data(patient1)
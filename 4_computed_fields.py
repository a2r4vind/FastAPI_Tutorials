from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):

    name: str
    age: int
    weight: float
    height: float
    married: bool
    allergies: List[str]
    email: EmailStr
    contact: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi_value = self.weight / ((self.height) ** 2)
        return round(bmi_value, 2)
    
def update_patient_data(patient: Patient):
    # simulate updating patient data into a database
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.email)
    print(patient.contact)
    print(f"BMI: {patient.bmi}")
    print("Patient data updated successfully.")

patient_info = {'name': 'john doe', 'age': 70, 'weight': 70.5, 'height': 1.75, 'married': False, 'allergies':['peanuts'], 'email': 'john@example.com', 'contact': {'phone': '1234567890'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)
from pydantic import BaseModel 

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    age: int
    address: Address

address_info = {'city': 'Surat', 'state': 'Gujarat', 'pin': '395001'}
address1 = Address(**address_info)

patient_info = {'name': 'John Doe', 'age': 30, 'address': address1}
patient1 = Patient(**patient_info)

print(patient1)
print(patient1.name)
print(patient1.age)
print(patient1.address.city)
print(patient1.address.state)
print(patient1.address.pin)
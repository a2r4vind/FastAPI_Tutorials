from pydantic import BaseModel 

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    age: int
    married: bool = False
    address: Address

address_info = {'city': 'Surat', 'state': 'Gujarat', 'pin': '395001'}
address1 = Address(**address_info)

patient_info = {'name': 'John Doe', 'age': 30, 'address': address1}
patient1 = Patient(**patient_info)

temp = patient1.model_dump()
print(temp)
print(type(temp))

temp_json = patient1.model_dump_json()
print(temp_json)
print(type(temp_json))

temp2 = patient1.model_dump(include={'name', 'age'})
print(temp2)

temp3 = patient1.model_dump(exclude={'age'})
print(temp3)

# exclude state from address while dumping
temp4 = patient1.model_dump(exclude={'address': {'state'}})
print(temp4)

# exclude those fields which are not set while creating pydantic model
temp5 = patient1.model_dump(exclude_unset=True) # this will not include married field
print(temp5)
from pydantic import BaseModel
from typing import List,Dict,Optional

class Patient(BaseModel):
    name:str
    age:int
    married:bool
    weight:float
    allergies:Optional[List[str]]=None
    contact_details:Dict[str,str] 

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print(patient.weight)
    print(patient.allergies)
    print(patient.contact_details)
    print("Inserted")
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print(patient.weight)
    print(patient.allergies)
    print(patient.contact_details)
    print("Updated")
##Here all the fields are mandatory cant leave any field

patient_info={'name':'Nitish','age':30,'married':True,'weight':75.2,'contact_details':{'phone':'12345','email':'krk@123'}}

patient1=Patient(**patient_info)
insert_patient_data(patient1)
update_patient_data(patient1)
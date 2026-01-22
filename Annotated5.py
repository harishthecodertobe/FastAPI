from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name:Annotated[str, Field(max_length=50,title='Name of the patient', description='Give full name of the patient', example='A Harish Kumar Dora')]
    email:EmailStr
    linkedln_profile:AnyUrl
    age:int = Field(gt=0,lt=120)
    married:Annotated[bool, Field(title='Marital Status', description='Is the patient married or not', example=True, default=False)]
    weight:float = Field(gt=0)
    allergies:Optional[List[str]]= Field(max_length=5,default=None)
    contact_details:Dict[str,str] 

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linkedln_profile)
    print(patient.age)
    print(patient.married)
    print(patient.weight)
    print(patient.allergies)
    print(patient.contact_details)
    print("Inserted")
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linkedln_profile)
    print(patient.age)
    print(patient.married)
    print(patient.weight)
    print(patient.allergies)
    print(patient.contact_details)
    print("Updated")
##Here all the fields are mandatory cant leave any field
##Here we can add customtypes like age should be positive int,email should be valid email format,url should be valid url format 
patient_info={'name':'Nitish','email':'harish@133.com','linkedln_profile':'https://www.linkedin.com/in/nitish-kumar-123456789','age':30,'married':True,'weight':75.2,'contact_details':{'phone':'12345','email':'krk@123'}}

patient1=Patient(**patient_info)
insert_patient_data(patient1)
update_patient_data(patient1)
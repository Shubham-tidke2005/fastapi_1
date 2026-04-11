from pydantic import BaseModel,Field,EmailStr,AnyUrl,field_validator
from typing import List,Dict,Annotated,Optional


#Understanding field validator

class Patient(BaseModel):
    name:Annotated[str,Field(max_length=25,title='enter the name of patient',description='this is description',examples=['ram','sham'])]
    age:float=Field(gt=0,lt=120)
    email:EmailStr
    url:AnyUrl
    weight:float=Field(gt=0)
    height:int
    allergies: Annotated[Optional[List[str]], Field(max_length=5)] = None
    contact_dit:Dict[str,str]
    
    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domain=['icic.com','hdfc.com'] 
        sep_domain=value.split('@')[-1]
        if sep_domain not in valid_domain:
            raise ValueError('not a valid domain')
        else:
            return value
    
    @field_validator('name')
    @classmethod
    def tranf_name(cls,value):
        return value.upper()
    


def insert_data(obj:Patient):
    print(obj.name)
    print(obj.age)
    print(obj.email)
    print(obj.url)
    print(obj.weight)
    print(obj.height)
    print(obj.allergies)
    print(obj.contact_dit)
    
dic={'name':'shubham','age':20,'email':'stidke826@icic.com','url':'https://github.com/','weight':40.5,'height':175,'allergies':['xyyz','sds'],'contact_dit':{'address':'nashik','phone':'12121312'}}

pt1=Patient(**dic)

insert_data(pt1)
    
    

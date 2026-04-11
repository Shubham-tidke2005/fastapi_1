from pydantic import BaseModel,Field,EmailStr,AnyUrl,model_validator
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
    
    @model_validator(mode='after')
    def emergency_alert(cls,model):
        if model.get("age", 0) > 60 and "emergency" not in model.get("contact_dit", {}):
            raise ValueError('age gtt than 60 should have emergency no.')
        else:
            return model


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
    
    

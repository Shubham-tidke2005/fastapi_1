from pydantic import BaseModel,Field,EmailStr,AnyUrl
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name:Annotated[str,Field(max_length=25,title='enter the name of patient',description='this is description',examples=['ram','sham'])]
    age:float=Field(gt=0,lt=120)
    email:EmailStr
    url:AnyUrl
    weight:float=Field(gt=0)
    height:int
    allergies:Optional[List[str]]=None,Field(max_length=5)
    contact_dit:Dict[str,str]

def insert_data(obj:Patient):
    print(obj.name)
    print(obj.age)
    print(obj.email)
    print(obj.url)
    print(obj.weight)
    print(obj.height)
    print(obj.allergies)
    print(obj.contact_dit)
    
dic={'name':'shubham','age':20,'email':'stidke826@gmail.com','url':'https://github.com/','weight':40.5,'height':175,'allergies':['xyyz','sds'],'contact_dit':{'address':'nashik','phone':'12121312'}}

pt1=Patient(**dic)

insert_data(pt1)
    
    
    


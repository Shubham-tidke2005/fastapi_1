from pydantic import BaseModel,Field,EmailStr,AnyUrl,computed_field
from typing import List,Dict,Annotated,Optional


#Understanding field validator

class Patient(BaseModel):
    name:str
    age:float=Field(gt=0,lt=120)
    email:EmailStr
    url:AnyUrl
    weight:float=Field(gt=0)  #kg
    height:int                #m
    allergies: Annotated[Optional[List[str]], Field(max_length=5)] = None
    contact_dit:Dict[str,str]
    
    @computed_field()
    @property
    def cal_bmi(self)->float:
        height_m=self.height/100
        bmi=round((self.weight/height_m**2),2)
        return bmi
    
    

def insert_data(obj:Patient):
    print(obj.name)
    print(obj.age)
    print(obj.email)
    print(obj.url)
    print(obj.weight)
    print(obj.height)
    print('Bmi: ',obj.cal_bmi)
    print(obj.allergies)
    print(obj.contact_dit)
    
dic={'name':'shubham','age':20,'email':'stidke826@icic.com','url':'https://github.com/','weight':40.5,'height':175,'allergies':['xyyz','sds'],'contact_dit':{'address':'nashik','phone':'12121312'}}

pt1=Patient(**dic)

insert_data(pt1)
    
    

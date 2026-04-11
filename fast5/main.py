#POST METHOD USE TO ADD NEW DATA INTO THE DATABASE
import json 
from fastapi import FastAPI,Path,HTTPException,Query
from typing import Annotated,List,Dict,Literal
from pydantic import BaseModel,Field,computed_field

#first we have to check the data type and the data of each field 
class petient(BaseModel):
    id:Annotated[str,Field(max_length=5)]
    name:Annotated[str,Field(description='enter the name')]
    city:Annotated[str,Field(description='enter the city')]
    age:Annotated[int,Field(gt=0,lt=120,description='enter the age')]
    gender:Annotated[Literal['Male','Female','other'],Field(description='enter gender')]
    weight:Annotated[float,Field(gt=0,lt=400,description='enter the weight')]
    height:Annotated[float,Field(gt=0,lt=200,description='enter the height')]
    
    @computed_field
    @property
    def bmi(self)->float:
        hh=self.height/10
        bm=self.weight/(hh**2)
        return bm
    
    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi < 18.5:
            return "Underweight"
        elif 18.5 <= self.bmi < 25:
            return "Healthy"
        elif 25 <= self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"
       

app=FastAPI()


def load_data():
    with open('data.json','r') as f:
        infoo=json.load(f)
    return infoo      #returns the dictionary

def save_data(dataa):
    with open('data.json','w') as f:
        json.dump(dataa,f)
    

@app.get('/')
def hell():
    return {"message":"API for storing patient info"}


@app.get('/about')
def ab():
    return {"INFORMATION OF SYSTEM"}


#details of all patients
@app.get('/details')
def dett():
    info=load_data()
    return info

@app.post('/addnew')
def addd(pt:petient):
    data=load_data()
     
    idd=pt.id
    if idd not in data:
        data[idd]=pt.model_dump(exclude=['id'])
    else:
        raise HTTPException(status_code=400,detail='patient already exits')
    
    save_data(data)



#PUT METHOD USE TO UPDATE PRESENT IN DATABASE 
#DELETE METHOD IS USE TO DELETE THE DATA FROM DATABASE
import json 
from fastapi.responses import JSONResponse
from fastapi import FastAPI,Path,HTTPException,Query
from typing import Annotated,List,Dict,Literal,Optional
from pydantic import BaseModel,Field,computed_field

#first we have to check the data type and the data of each field 
#WE DOES NOT NEED COMPUSORY DATA IN EACH FIELD(...,)
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
        hh=self.height/100
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
        
        
        
class petientupdate(BaseModel):
    name:Annotated[Optional[str],Field(default=None)]
    city:Annotated[Optional[str],Field(description='enter the city',default=None)]
    age:Annotated[Optional[int],Field(gt=0,lt=120,description='enter the age',default=None)]
    gender: Annotated[Optional[Literal['Male', 'Female', 'other']],Field(default=None)]

    weight:Annotated[Optional[float],Field(gt=0,lt=400,description='enter the weight',default=None)]
    height:Annotated[Optional[float],Field(gt=0,lt=200,description='enter the height',default=None)]
    
   
       

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



@app.put('/update/{id}')
def funnn(id:str,update_det:petientupdate):
    data=load_data()
    
    if id not in data:
        raise HTTPException(status_code=404,detail='id does not exits')
    
    existing_info=data[id]
    new_info=update_det.model_dump(exclude_unset=True)
    for k,val in new_info.items():
        existing_info[k]=val
    existing_info['id']=id
    pt_ex_obj=petient(**existing_info)
    existing_info=pt_ex_obj.model_dump(exclude='id')
    
    data[id]=existing_info
    
    
    save_data(data)
    
    return JSONResponse(status_code=200,content={'message':'we did it'})



@app.delete('/del/{pid}')
def delll(pid:str):
    data=load_data()
    
    if pid not in data:
        raise HTTPException(status_code=404,detail='user not found')
    
    del data[pid]
    
    save_data(data)
    
    return JSONResponse(status_code=200,content={'message':'deleted sucessfull!'})
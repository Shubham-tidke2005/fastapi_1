import json 
from fastapi import FastAPI,Path,HTTPException,Query

app=FastAPI()

def load_data():
    with open('data.json','r') as f:
        infoo=json.load(f)
    return infoo      #returns the dictionary

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


#details of specfic patient using path parameter or by using docs
#http://127.0.0.1:8000/patient/P001
@app.get('/patient/{pid}')
def getspe(pid:str=Path(...,description='enter patient id',example='P001')):
    dictt=load_data()
    if pid in dictt:
        return dictt[pid]
    else: 
        raise HTTPException(status_code=404,detail="patient not fount")
    
    

#QUERY PARAMETER
#http://127.0.0.1:8000/sortt?sort_by=bmi&order=desc
@app.get('/sortt')
def st(sort_by:str=Query(...,description="sort on the basis of height weight and bmi"),order:str=Query('asc',description="enter asc od desc")):
    lis=['height','weight','bmi']
    if sort_by not in lis or order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail='invalid input!')
    
    odderr=True if order=='asc' else False 
    
    data=load_data()
    sorted_data= dict(sorted(data.items(), key=lambda x: x[1][sort_by], reverse=odderr))
    return sorted_data
        
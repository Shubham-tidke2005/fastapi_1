from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd
import pickle
from pydantic import BaseModel,Field,computed_field
from typing import Annotated

app=FastAPI()


tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]

tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]


#bmi,age_group,lifestyle_risk,city_tier,income_lpa,occupation  (req for dataframe)

class UserInput(BaseModel):
    age:Annotated[int,Field(...,gt=0,lt=120,description='Age of user')]
    weight:Annotated[float,Field(...,gt=0,lt=300,description='weight of user')]
    height:Annotated[float,Field(...,gt=0,lt=2.5,description='height of user')]
    income_lpa:Annotated[float,Field(...,description='income in lpa of user')]
    smoker:Annotated[bool,Field(...,description='Is user is smoker')]
    city:Annotated[str,Field(...,description='city of user')]
    occupation:Annotated[str,Field(...,description='occupation of user')]
    
    @computed_field
    @property
    def bmi(self)->float:
        return self.weight/(self.height**2)
    
    @computed_field
    @property
    def lifestyle_risk(self)->str:
        if self.smoker and self.bmi>30:
            return 'high'
        elif self.smoker and self.bmi>27:
            return 'medium'
        else:
            return 'low'
        
    @computed_field
    @property
    def age_group(self)->str:
        if self.age <25:
            return 'young'
        elif self.age <45:
            return 'adult'
        elif self.age <60:
            return 'middle_aged'
        else:
            return 'senior'
        
    @computed_field
    @property
    def city_tier(self)->int:
        # Feature 4: City Tier
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3



@app.get('/')
def hello():
    return {"message":"wellcome to my first ML model"}


#bmi,age_group,lifestyle_risk,city_tier,income_lpa,occupation  (req for dataframe)


with open('model.pkl','rb') as f:
    model=pickle.load(f)

@app.post('/predict')
def predictt(user_in:UserInput):
    df=pd.DataFrame([{
            'bmi':user_in.bmi,
            'age_group':user_in.age_group,
            'lifestyle_risk':user_in.lifestyle_risk,
            'city_tier':user_in.city_tier,
            'income_lpa':user_in.income_lpa,
            'occupation':user_in.occupation
                     }])
    prediction=model.predict(df)[0]
    
    return JSONResponse(status_code=200,content={'PREDICTION IS: ':prediction})
from pydantic import BaseModel,Field,computed_field,field_validator
from typing import Annotated
from config.city_tire import tier_1_cities,tier_2_cities 
#bmi,age_group,lifestyle_risk,city_tier,income_lpa,occupation  (req for dataframe)

class UserInput(BaseModel):
    age:Annotated[int,Field(...,gt=0,lt=120,description='Age of user')]
    weight:Annotated[float,Field(...,gt=0,lt=300,description='weight of user')]
    height:Annotated[float,Field(...,gt=0,lt=2.5,description='height of user')]
    income_lpa:Annotated[float,Field(...,description='income in lpa of user')]
    smoker:Annotated[bool,Field(...,description='Is user is smoker')]
    city:Annotated[str,Field(...,description='city of user')]
    occupation:Annotated[str,Field(...,description='occupation of user')]
    
    
    #I want first letter of city to be capital
    @field_validator('city')
    @classmethod
    def concity(cls,v:str)->str:
        v=v.strip().capitalize()
        return v
    
    
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


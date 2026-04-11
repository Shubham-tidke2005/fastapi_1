from pydantic import BaseModel


#the python generally does not understand the data type
def insert_data(name,age):
    print('name: ',type(name))
    print('age: ',type(age))
    
insert_data('shubham','20')


#suppose we have to write code for this
def insert_dataa(name:str,age:int):
    if type(name)==str and type(age)==int:
        if(age>0 and age<120):
            print('we can insert this data into database')
        else:
            print('age is out of range')
    else:
        print('invalid type!!')
        
insert_dataa('shubham','20')
#for redusing such code and checking datatype we use pydantic 


#using pydantic
class infoo(BaseModel):
    name:str
    age:int

def insert_dataaa(inf:infoo):
    print('using pydantic modelll')
    print(type(inf.name))
    print(type(inf.age))                     #automatic conversion
    print('inserted dataaaaa') 
    
dictt={'name':'shubham','age':'20'}
p1=infoo(**dictt)

insert_dataaa(p1)



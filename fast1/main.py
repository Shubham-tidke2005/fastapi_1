from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def hello():
    return {'message':"Wellcome to FastApi"}

@app.get('/goo')
def ggg():
    return {'message':"LET'S GO!"}
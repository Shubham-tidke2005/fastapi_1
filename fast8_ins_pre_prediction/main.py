from fastapi import FastAPI # type: ignore
from fastapi.responses import JSONResponse # type: ignore
from schema.user_input import UserInput
from model.predict import MODEL_VERSION,model,predicted_output

app=FastAPI()

@app.get('/')
def hello():
    return {"message":"Insurance Premium Prediction"}


#this is api for machine (used during deployment(aws)) to check api is working correctly 
@app.get('/health')
def helth_cheak():
    return {
        'status':'OK',
        'version':MODEL_VERSION,
        'model_loaded':model is not None
    }

#bmi,age_group,lifestyle_risk,city_tier,income_lpa,occupation  (req for dataframe)


@app.post('/predict')
def predictt(user_in:UserInput):
    user_dictt={
            'bmi':user_in.bmi,
            'age_group':user_in.age_group,
            'lifestyle_risk':user_in.lifestyle_risk,
            'city_tier':user_in.city_tier,
            'income_lpa':user_in.income_lpa,
            'occupation':user_in.occupation
            }
    try:
        prediction=predicted_output(user_dictt)
        return JSONResponse(status_code=200,content={'PREDICTION IS: ':prediction})
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))
        
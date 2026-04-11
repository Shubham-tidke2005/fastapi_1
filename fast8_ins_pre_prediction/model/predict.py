import pandas as pd
import pickle

#MLflow automatic calculate this while working on real time projects
MODEL_VERSION='1.0.0'

with open('model/model.pkl','rb') as f:
    model=pickle.load(f)
    


class_labels=model.classes_.tolist()

def predicted_output(userinsputt:dict):
    df=pd.DataFrame([userinsputt])
    outputt=model.predict(df)[0]
    
    probabilities=model.predict_prob(df)[0]
    confidance=max(probabilities)
    
    #creating maping:{class_name:probability}
    class_probs=dict(zip(class_labels,map(lambda p:round(p,4),probabilities)))
    
    return {
        
    }
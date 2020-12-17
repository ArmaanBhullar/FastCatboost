from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import uvicorn

app = FastAPI()

from catboost import CatBoostClassifier
model = CatBoostClassifier()
model.load_model('/home/armaan/Desktop/flask_docker/model_v2.bin')
df = pd.read_csv('~/Desktop/flask_docker/training_data.csv')

class Data(BaseModel):
    A: float
    B: float


@app.post("/predict")
def predict(data: List[Data]):
    print(f"Data is {data}")
    list_data = [d.dict() for d in data]
    print(list_data)
    df_data = pd.DataFrame.from_records(list_data)
    print(df_data)
    print(model.feature_names_)
    print(df_data[model.feature_names_])
    predictions = model.predict(df_data[model.feature_names_])
    return {'predictions': {'predicted_value': pred for pred in
        list(predictions)}}

@app.get("/")
def read_root():
    return {"Hello": "Armaan"}


#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Optional[str] = None):
#    return {"item_id": item_id, "q": q}



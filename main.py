from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Item(BaseModel):
    name: str
    year: int
    selling_price: int
    km_driven: int
    fuel: str
    seller_type: str
    transmission: str
    owner: str
    mileage: str
    engine: str
    max_power: str
    torque: str
    seats: float


class Items(BaseModel):
    objects: List[Item]


@app.post("/predict_item")
def predict_item(item: Item) -> float:
    data = pd.DataFrame([item.dict()])
    data.drop(['selling_price','name','torque'], axis = 1, inplace = True)
    for i in ['mileage','engine','max_power']:
      data[i] = [float(j) for j in list(map((lambda x: ''.join(re.findall(r'[\d\.-]', str(x)))), data[i]))]
    for i in ['engine','seats']:
      data[i] = data[i].astype(int)
    data = data.select_dtypes('number')
    pred = model1.predict(data)
    return float(pred[0])


@app.post("/predict_items")
def predict_items(items: List[Item]) -> List[float]:
    data1 = pd.read_csv(items)
    data1.drop(['selling_price','name','torque'], axis = 1, inplace = True)
    for i in ['mileage','engine','max_power']:
      data1[i] = [float(j) for j in list(map((lambda x: ''.join(re.findall(r'[\d\.-]', str(x)))), data1[i]))]
    for i in ['engine','seats']:
      data1[i] = data1[i].astype(int)
    pred2 = best.predict(data1)
    data1['selling_price'] = pred2
    data1.to_csv('prediction.csv', index = False)
    return data1

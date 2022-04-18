import pandas as pd
from fastapi import FastAPI
from utils import *

APP_VERSION = "1.0.0"
APP_NAME = "Recommendation Engine"
API_PREFIX = "/"
DATA_PATH = "data/"

user_user_sim_matrix = pd.read_parquet(
    DATA_PATH+'user_user_sim_matrix.parquet')
item_item_sim_matrix = pd.read_parquet(
    DATA_PATH+'item_item_sim_matrix.parquet')
customer_item_matrix = pd.read_parquet(
    DATA_PATH+'customer_item_matrix.parquet')
df = pd.read_parquet(DATA_PATH+'df.parquet')


app = FastAPI(title="Recommendation Engine",  version=APP_VERSION,
              description="This API is built for Recommendation Engine Backend services.")


@app.get("/", status_code=200, summary="Returns 200 for healthcheck.", tags=["root"])
def index():
    return {"staus": "ok"}


@app.get("/predict/user/{user_id}", summary="Returns user-based recommendations", response_description="User Based Recommendation Results.", tags=["prediction"])
async def predict(user_id: str = '12350', n: int = 5):

    pred = recommend_customer(user_user_sim_matrix,
                              customer_item_matrix, df, user_id, n=n)

    return {"success": True, "type": "user_based", "total": n, "data": {user_id: str(pred)}}


@app.get("/predict/item/{item_id}", summary="Returns item-based recommendations", response_description="Item Based Recommendation Results.", tags=["prediction"])
async def predict(item_id: str = '23166', n: int = 5):

    pred = get_similar_items(item_item_sim_matrix, item_id, n=n)

    return {"success": True, "type": "item_based", "total": n, "data": {item_id: str(pred)}}

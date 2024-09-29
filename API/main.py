from datetime import datetime
from copy import deepcopy

import psycopg
from fastapi import FastAPI

from queries import queries

app = FastAPI()

conn = psycopg.connect(dbname="sensordata",
                       host="85.215.48.7",
                       user="postgres",
                       password="admin123",
                       port="5432")
cursor = conn.cursor()

fakeData = [
    {"timestmp": "2024-09-27 17:51:00", "temperature": 22},
    {"timestmp": "2024-09-27 17:51:10", "temperature": 22},
    {"timestmp": "2024-09-27 17:51:20", "temperature": 22},
    {"timestmp": "2024-09-27 17:51:30", "temperature": 22},
    {"timestmp": "2024-09-27 17:51:40", "temperature": 22},
    {"timestmp": "2024-09-27 17:51:50", "temperature": 22},
    {"timestmp": "2024-09-27 17:52:00", "temperature": 22}
]

DATETIME_DEFAULT_FORMAT = "%Y-%m-%d %H:%M:%S"

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/data/")
def get_data(timerange: str):
    data = deepcopy(fakeData)
    print(data)

    match timerange:
        case "Hour":
            target_format = "%H:%M:%S"
        case _:
            target_format = DATETIME_DEFAULT_FORMAT

    id_iterator = 0
    for data_item in data:
        data_item["id"] = id_iterator
        data_item["timestmp"] = datetime.strptime(data_item["timestmp"], DATETIME_DEFAULT_FORMAT).strftime(target_format)

    return data

conn.close()
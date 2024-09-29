from fastapi import FastAPI

app = FastAPI()

fakeData = [
    {"id": 1, "timestmp": "2024-09-27 17:51:00", "temperature": 22},
    {"id": 2, "timestmp": "2024-09-27 17:51:10", "temperature": 22},
    {"id": 3, "timestmp": "2024-09-27 17:51:20", "temperature": 22},
    {"id": 4, "timestmp": "2024-09-27 17:51:30", "temperature": 22},
    {"id": 5, "timestmp": "2024-09-27 17:51:40", "temperature": 22},
    {"id": 6, "timestmp": "2024-09-27 17:51:50", "temperature": 22},
    {"id": 7, "timestmp": "2024-09-27 17:52:00", "temperature": 22}
]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/data/")
def get_data(timerange: str):
    return fakeData
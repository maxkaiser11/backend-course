from fastapi import FastAPI

app = FastAPI()


@app.get("/shipment/{id}")
def get_shipment(id: int):
    return {"id": id, "content": "wooden table", "status": "in transit"}

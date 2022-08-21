import pandas as pd

from typing import List, Optional
from pydantic import BaseModel
from fastapi import FastAPI

from src.util.algo1 import add_int

import logging

logging.basicConfig(level='DEBUG')
logger = logging.getLogger(__name__)

app = FastAPI()


class AlgoInputs(BaseModel):
    # depend on python version3.9?? https://fastapi.tiangolo.com/tutorial/body-nested-models/
    input1: float
    input2: float


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/algotest/{id}")
async def run_vicc(algoInput: AlgoInputs):

    res = add_int(algoInput.input1, algoInput.input2)

    return {"inputs": [algoInput.input1, algoInput.input2], "results": res}


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")

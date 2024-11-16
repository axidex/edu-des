from fastapi import FastAPI

from src.des import Des

app = FastAPI()


@app.post("/encrypt")
def read_root(data: str, key: str):
    # data = "03000e00"
    # key = "0b1401"

    des = Des()
    des.encrypt(data, key)
    # print('\n'.join(des.steps))

    return '\n'.join(des.steps)

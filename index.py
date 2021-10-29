# python -m uvicorn index:app --reload

from math import trunc
from typing import Optional
from fastapi import FastAPI, Request, APIRouter, Header
from routes.users import users, allusers
from func.authcheck import checkauthtime, tokens, updateoldtk
import string
import random
import time

# tokens = []
# alluser = []

app = FastAPI()


@app.get("/")
async def home():
    return {"Hello": "World"}


@app.post("/login")
async def login(req: Request):
    global allusers
    req = await req.json()
    t = req["user"]
    for tp in allusers:
        if tp["user"] == t:
            auth_t = await createauth(t)
            return {"login": "success", "auth-token": auth_t}
    return {"login": "fail"}

@app.get("/alltokens")
async def profile(req: Request):
    global tokens
    return {"alltokens": tokens}


async def createauth(x):
    # global tokens
    chars = ""
    size = 16
    for _ in range(size):
        chars += random.choice(
            string.ascii_uppercase + string.digits + string.ascii_lowercase + "#$%_-+"
        )
    t = time.time()
    t = t + (60*60*24)  # 24 Hours token timeout (ss * mm * hh)
    # t=t+60*1    # 1 minute token timeout
    t = str(int(t))
    # print(t)
    chars = (
        chars[:4]
        + t[:2]
        + chars[4:6]
        + t[2:5]
        + chars[6:9]
        + t[5:8]
        + chars[9:]
        + t[8:]
    )
    # tokens.append({x:chars})
    tk = await updateoldtk(x, chars)
    # tokens  += [{x:chars}]
    # print(tk)
    return chars


@app.post("/profile")
async def profile(req: Request):
    head = req.headers["auth-token"]
    # print(head)
    u_data = await req.json()
    u = u_data["user"]
    t = await checkauthtime(head, u)
    if t:
        return {"user ": u + " profile"}
    else:
        return {"user ": u + " unauthorized"}


app.include_router(users, prefix="/users")

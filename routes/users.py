from fastapi import FastAPI, APIRouter, Request

# from ..index import allusers
from func.authcheck import checkauthtime

users = APIRouter()
allusers = []


@users.get("/")
async def profile(req: Request):
    head = req.headers["auth-token"]
    u_data = await req.json()
    u = u_data["user"]
    t = await checkauthtime(head, u)
    if t:
        return {"user": u}
    else:
        return {"NA"}


@users.get("/all")
async def profile(req: Request):
    global allusers
    return {"allusers": allusers}


@users.post("/new")
async def register(req: Request):
    global allusers
    p=allusers
    req = await req.json()
    if "user" in req and "password" in req:
            t = {"user": req["user"], "password": req["password"]}
            # p.append(t)
            allusers += t
            # allusers=p
            print(allusers)
            return {"success": "user " + req["user"] + " added"}
    return {"fail": "user not added"}

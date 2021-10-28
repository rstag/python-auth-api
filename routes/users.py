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


@users.post("/new")
async def register(req: Request):
    global allusers
    req = await req.json()
    if "user" in req and "password" in req:
            t = {"user": req["user"], "password": req["password"]}
            allusers.append(t)
            return {"success": "user added"}
    return {"fail": "user not added"}

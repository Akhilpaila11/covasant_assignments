from fastapi import FastAPI, Request, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy import create_engine, text
from typing import Optional

app = FastAPI()

DATABASE = "people.db"

def get_db():
    return create_engine(f"sqlite:///{DATABASE}")

class NotFound(Exception):
    pass


def get_all_people():
    engine = get_db()
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT name, age FROM people")
        ).fetchall()
        return result
        
def get_age(name: str):
    engine = get_db()
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT age FROM people WHERE name = :name"),
            {"name": name}
        ).fetchone()
        if result:
            return result[0]
        else:
            raise NotFound()


# Pydantic model to define expected request body for POST
class HelloRequest(BaseModel):
    name: str
    format: str

@app.get("/helloj")
async def helloj_get(
    query_name: Optional[str] = Query("abc"),
    query_format: Optional[str] = Query("json")
):
    # This handles the GET method
    return fetch_helloj(query_name, query_format)


@app.post("/helloj")
async def helloj_post(request: HelloRequest):
    # This handles the POST method, where HelloRequest is the parsed body
    return fetch_helloj(request.name, request.format)


@app.get("/helloj/{name}/{format}")
async def helloj_path(name: str, format: str):
    return fetch_helloj(name, format)


@app.get("/helloj/all")
async def get_all_persons():
    people = get_all_people()
    if people:
        # If people found, return them
        return JSONResponse(content={"people": [{"name": person[0], "age": person[1]} for person in people]}, status_code=200)
    else:
        # If no people are found
        return JSONResponse(content={"details": "No people found"}, status_code=404)


def fetch_helloj(fname: str, fformat: str):
    try:
        age = get_age(fname)
        return JSONResponse(content={"name": fname, "age": age}, status_code=200)
    except NotFound:
        return JSONResponse(content={"name": fname, "details": "Not found"}, status_code=500)

from fastapi import FastAPI, Query
from pydantic import BaseModel
from enum import Enum
from typing import Optional


app = FastAPI(
    title="Query and Paramters",
    description="A Demo Example displays the use of Path Paramters and Query parameters."
)

class Month(str, Enum):
    January = "January"
    February = "February"
    March = "March"
    Apr = "Apr"
    May = "May"
    June = "June"
    July = "July"
    August = "August"
    September =  "September"
    October = "October"
    November = "November"
    December = "December"


class State(Enum):
    Draft = "Draft"
    Posted = "Posted"


class Post(BaseModel):
    title: str
    description: str
    state: Optional[State]


@app.get("/")
def index():
    return {"message": "Hello World"}

@app.get("/post/{post_id}")
def get_post(post_id: int):
    """
    Here the `post_id` can only be integer and not anything else.
    """
    return {'post_id': post_id}

@app.get("/posts/{month}")
def get_monthly_posts(month: Month):
    """
    `month` values is Permited only from `Enum` class Defained for it.
    """
    return {"month": month , "posts": []}

@app.get("/posts")
def get_posts(skip: int = Query(default=0, ge=0), limit: int = Query(default=80, le=80)):
    """
    Filter `Posts` based on the query parameter of `skip` and `limit`.
    """
    return  {"skip": skip, "limit": limit}

@app.post("/post")
def create_post(post: Post):
    """
    Create a `Post` based on the data received in the `Request Body`.
    """
    return post

@app.put("/post/{post_id}")
def update_post(post_id: int, post: Post):
    """
    Update the Post based on the values received in `Request Body` for the given `post_id`
    """
    return {"post_id":post_id, "post": post}

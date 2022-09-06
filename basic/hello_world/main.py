from fastapi import FastAPI

app = FastAPI(
    title="Hello World",
    description="A Hello World Application in FastAPI."
)


@app.get("/")
def index():
    """
    A Simple GET Request for this app.
    """
    return {"message": "Hello World !"}

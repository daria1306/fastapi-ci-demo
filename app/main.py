from fastapi import FastAPI

app = FastAPI(title="CI Demo API")


@app.get("/")
def root():
    return {"message": "Hello, CI!"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/sum")
def sum_numbers(a: int, b: int):
    return {"result": a + b}
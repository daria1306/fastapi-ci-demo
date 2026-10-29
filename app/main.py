@app.get("/")
def root():
    return {"message": "Bye"}
from fastapi import FastAPI

app = FastAPI(
    title="Salary"
)



@app.get("/")
def index():
    return "hello world"
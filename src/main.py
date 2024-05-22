from fastapi import FastAPI

import uvicorn

from users.views import router as users_router

app = FastAPI()
app.include_router(users_router)


@app.get("/")
def hello_index():
    return {
        "message": "Hello index!",
    }


@app.get("/hello/")
def hello(name: str = "World"):
    name = name.strip().title()
    return {"message": f"Hello {name}!"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

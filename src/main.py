from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from fastapi_users import FastAPIUsers, fastapi_users
from fastapi_users.authentication import Authenticator
import uvicorn
from src.auth.manager import get_user_manager
from src.auth.schemas import UserCreate, UserRead
from src.auth.auth import auth_backend
from src.database import User

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
authenticator = Authenticator([auth_backend], get_user_manager)


# @app.post("/auth/jwt/login/")
# async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
#     return {"token": token}


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)


app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


current_user = fastapi_users.current_user()
current_active_user = fastapi_users.current_user(active=True)
current_active_verified_user = fastapi_users.current_user(active=True, verified=True)


@app.get("/protected-route")
def protected_route(user: User = Depends(current_active_verified_user)):
    """https://fastapi-users.github.io/fastapi-users/10.1/usage/current-user/"""
    return f"Hello, {user.username}"


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

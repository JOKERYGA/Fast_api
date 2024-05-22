from pydantic import BaseModel, EmailStr
from typing import Annotated
from annotated_types import MinLen, MaxLen


class CreateUser(BaseModel):
    id : int
    # username: str =Field(..., min_lenght=3, max_lenght=30)
    username: Annotated[str, MinLen(3), MaxLen(30)]
    email: EmailStr
    salary: str

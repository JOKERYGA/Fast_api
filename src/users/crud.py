from users.schemas import CreateUser

def create_user(user_in: CreateUser):
    user = user_in.model_dump()
    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "salary": user.salary
    }
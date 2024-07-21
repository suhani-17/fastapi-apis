from fastapi import FastAPI, HTTPException
from uuid import UUID, uuid4
from typing import List
from models import User, Gender, Role, UserUpdateModel

app = FastAPI()

db: List[User] = [
    User(
        id=UUID('a4ad0a7b-95b8-489f-bc24-8a9feda48555'),
        first_name='suhani',
        last_name='jain',
        middle_name=None, 
        gender=Gender.female,
        roles=[Role.student, Role.user]
    ),

    User(
        id=UUID('0eb12230-5028-4bed-9b37-14744dc45411'),
        first_name='taylor',
        last_name='swift',
        middle_name=None, 
        gender=Gender.female,
        roles=[Role.admin, Role.student]
    ),

    User(
        id=UUID('da53a6ad-3ce5-49ab-8d64-f1f84b9ab63f'),
        first_name='karan',
        last_name='aulja',
        middle_name=None, 
        gender=Gender.male,
        roles=[Role.user]
    ),

    User(
        id=UUID('22db3f2a-dca0-434b-8031-454cef98f06d'),
        first_name='ashima',
        last_name='sood',
        middle_name=None, 
        gender=Gender.female,
        roles=[Role.admin]
    )
]

@app.get('/')
def root():
    return {'Hello':'World'}

@app.get('/api/v1/users')
async def fetch_users():
    return db;

@app.post('/api/v1/users')
async def register_users(user:User):
    db.append(user)
    return {"id":user.id}

@app.delete('/api/v1/users/{user_id}')
async def delete_user(user_id:UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )

@app.put('/api/v1/users/{user_id}')
async def update_user(user_update: UserUpdateModel, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not"
    )
        
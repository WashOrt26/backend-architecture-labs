from fastapi import APIRouter, Depends
from sqlalchemy.orm import session
from pydantic import BaseModel
from data_base.conections import get_db, UserTable


# An isolated router to group API services
router = APIRouter(prefix="/api/v1", tags=["users"])

# payload validation model
#if the client does not send the correct data, the API will return a 422 error
class UserSchema(BaseModel):
    name: str
    email: str
    password: str

# Endpoint get
@router.get("/users")
def api_get_users(db: session = Depends(get_db)):
    users = db.query(UserTable).all()
    return users

# Endpoint post
@router.post("/users")
def api_create_user(user: UserSchema, db: session = Depends(get_db)):
    db_user = UserTable(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"status": "success", "user": db_user}


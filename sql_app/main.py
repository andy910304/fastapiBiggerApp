from fastapi import Depends, FastAPI, HTTPException, status
from .database import engine
from . import users
from . import posts

users.models.Base.metadata.create_all(bind=engine)
posts.models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.main.router)
app.include_router(posts.main.router)

# @app.post("/token", response_model=schemas.Token)
# async def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
#     user = crud.authenticate_user(db, form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = crud.create_access_token(
#         data={"sub": user.username}, expires_delta=access_token_expires
#     )
#     return {"access_token": access_token, "token_type": "bearer"}
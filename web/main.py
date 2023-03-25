from fastapi import FastAPI
from db import Base, engine
from addressbook.controllers.controller import app_router

Base.metadata.create_all(engine)
app = FastAPI()
app.include_router(app_router)

@app.get("/")
def root():
    return "Welcome to FastAPI Address Book"



# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)

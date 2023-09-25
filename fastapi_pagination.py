from fastapi import FastAPI
from pydantic import BaseModel, Field
import uvicorn
# import all you need from fastapi-pagination
from fastapi_pagination import Page, add_pagination, paginate

app = FastAPI()  # create FastAPI app


class UserOut(BaseModel):  # define your model
    name: str = Field(..., example="Steve")
    surname: str = Field(..., example="Rogers")


users = [ {"name":"Steve","surname":"Jobs"},{"name":"Bill","surname":"Gates"} ]


@app.get('/users', response_model=Page[UserOut])  # use Page[UserOut] as response model
async def get_users():
    return paginate(users)  # use paginate function to paginate your data


add_pagination(app)  # important! add pagination to your app

if __name__ == '__main__':
    uvicorn.run('ws:app')
    

from fastapi import FastAPI
from fastapi import HTTPException
import uvicorn
from funcs.users_db import db_connection, select



app = FastAPI()


@app.get('/{_id}')
async def index(_id: int):
    vcon = db_connection('Users.db')
    datas = select(vcon, _id)
    if datas:
        user_data = {
            'id': datas[0],
            'name': datas[1],
            'cpf': datas[2],
            'age': datas[3],
        }
        vcon.close()
        return user_data
    raise HTTPException(status_code=404, detail="User not found!")


if __name__ == '__main__':
    uvicorn.run(app='app:app', reload=True)



import uvicorn as uvicorn
from fastapi import FastAPI

from source.db.client import init_db
from source.secret.router import router as secret_router


app = FastAPI(title='onetime_secret')
app.include_router(secret_router)


@app.on_event('startup')
async def startup():
    await init_db()

if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=8080, reload=True)

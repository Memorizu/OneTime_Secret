import uvicorn as uvicorn
from fastapi import FastAPI
from source.secret.router import secret_router


app = FastAPI(title='onetime_secret')
app.include_router(secret_router)


if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=8080, reload=True)

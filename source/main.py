from contextlib import asynccontextmanager

import uvicorn as uvicorn
from fastapi import FastAPI

from source.db.client import init_db
from source.secret.router import router as secret_router
from source.settings import scheduler


@asynccontextmanager
async def lifespan(app: FastAPI):
    scheduler.start()
    await init_db()
    yield
    scheduler.shutdown()


app = FastAPI(title='onetime_secret', lifespan=lifespan)
app.include_router(secret_router)


if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=8080, reload=True)

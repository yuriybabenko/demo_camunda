from fastapi import FastAPI

from pages.pages import pages
from api.images import images
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/assets", StaticFiles(directory="assets"), name='assets')

app.include_router(pages)
app.include_router(images)
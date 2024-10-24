from fastapi import APIRouter
from fastapi.responses import FileResponse

pages = APIRouter()

@pages.get('/', response_class=FileResponse)
async def read_index():
    return FileResponse('app/pages/index.html')
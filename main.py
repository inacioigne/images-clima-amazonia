from pathlib import Path
from mimetypes import guess_type

from fastapi.responses import FileResponse
from fastapi import FastAPI


app = FastAPI(title="Images Clima Amazonia API", description="API para acessar imagens do clima na Amazônia", version="1.0.0")

IMAGE_DIR = Path("data").resolve()

@app.get("/{year}/{edition}/{session}/{image_name}")
async def read_item(year: int, edition: str, session: str,   image_name: str):
    image_path = Path(IMAGE_DIR, str(year), str(edition), session, image_name)
    media_type, _ = guess_type(str(image_path))
    return FileResponse(
        path=image_path,
        media_type=media_type or "application/octet-stream",
        filename=image_path.name
    )
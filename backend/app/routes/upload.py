from fastapi import APIRouter, UploadFile, File
import os

router = APIRouter()

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    # Save locally for now
    with open(f"uploads/{file.filename}", "wb") as f:
        f.write(content)
    return {"filename": file.filename, "status": "saved"}
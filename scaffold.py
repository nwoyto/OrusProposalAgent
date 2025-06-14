import os

folders = [
    "backend/app/routes",
    "backend/app/services",
    "backend/app/models",
    "frontend/src/components",
    "frontend/src/pages",
    "frontend/src/services"
]

files = {
    "backend/app/main.py": """from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import upload, agent, auth

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router, prefix="/upload")
app.include_router(agent.router, prefix="/agent")
app.include_router(auth.router, prefix="/auth")

@app.get("/")
def root():
    return {"message": "Orus Proposal Agent API is running"}
""",
    "backend/requirements.txt": "fastapi\nuvicorn[standard]\npython-multipart",
    "frontend/package.json": "{\n  \"name\": \"orus-proposal-agent\",\n  \"version\": \"0.1.0\"\n}"
}

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for path, content in files.items():
    with open(path, "w") as f:
        f.write(content)

print("Scaffold created.")
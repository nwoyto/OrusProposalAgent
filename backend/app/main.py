from fastapi import FastAPI
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

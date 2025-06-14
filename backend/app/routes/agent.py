from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class AgentPrompt(BaseModel):
    message: str

@router.post("/chat")
def talk_to_agent(prompt: AgentPrompt):
    # Mock response
    return {"response": f"Agent received: {prompt.message}"}
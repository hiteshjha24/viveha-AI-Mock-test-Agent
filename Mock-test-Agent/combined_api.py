from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent.mcq_agent import MCQAgent
from agent.coding_agent import CodingAgent
from agent.evaluation_agent import EvaluationAgent
from agent.coding_eval_agent import CodingEvaluationAgent
import uvicorn

app = FastAPI(title="Unified Interview Question Generator", version="1.1")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)


mcq_agent = MCQAgent()
coding_agent = CodingAgent()
evaluation_agent = EvaluationAgent()
coding_eval_agent = CodingEvaluationAgent()
class CodingRequest(BaseModel):
    company: str
    jrole: str
    topics: list[str]
    difficulty: str = "medium"

class MCQRequest(BaseModel):
    company: str
    jrole: str
    topics: list[str]
    difficulty: str = "medium"
    count: int = 5

class SubmissionItem(BaseModel):
    topic: str
    question: str
    user_answer: str
    correct_answer: str

class EvaluationRequest(BaseModel):
    submissions: list[SubmissionItem]


class CodeEvaluationRequest(BaseModel):
    question_title: str
    question_description: str
    user_code: str
    language: str = "python"

@app.post("/generate_coding")
def generate_coding(request: CodingRequest):
    try:
        data = {
            "company": request.company,
            "jrole": request.jrole,
            "topics": request.topics,
            "difficulty": request.difficulty,
        }
        result = coding_agent.run(data)
        return {"status": "success", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate_mcq")
def generate_mcq(request: MCQRequest):
    try:
        data = {
            "company": request.company,
            "jrole": request.jrole,
            "topics": request.topics,
            "difficulty": request.difficulty,
            "count": request.count
        }
        result = mcq_agent.run(data)
        return {"status": "success", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/evaluate_mcq")
def evaluate_mcq(request: EvaluationRequest):
    try:
        submission_data = [item.model_dump() for item in request.submissions]
        result = evaluation_agent.evaluate(submission_data)
        return {"status": "success", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.post("/evaluate_code_submission")
def evaluate_code_submission(request: CodeEvaluationRequest):
    try:
        result = coding_eval_agent.evaluate(request.model_dump())
        return {"status": "success", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
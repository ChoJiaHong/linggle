from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import main_config


from database import Repository


app = FastAPI(root_path="/db")


app.add_middleware(
    CORSMiddleware,
    allow_origins=main_config.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class hintModel(BaseModel):
    word: str


@app.post("/hint")
def hint(_hintModel: hintModel):
    hintWord = _hintModel.word.strip()
    if hintWord == " ":
        return []
    if hintWord.__contains__(" "):
        words = hintWord.split()
        return Repository.getWithPattern(hintWord=hintWord, words=words)
    return Repository.getWithTerm(hintWord=hintWord)




from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel


class Memo(BaseModel):
    id: str
    content: str


memos = []
app = FastAPI()


@app.post("/memos")
def create_memo(memo: Memo):
    memos.append(memo)
    return "추가 성공"


@app.get("/memos")
def read_memo():
    return memos


@app.put("/memos/{memo_id}")
def put_memo(req_memo: Memo):
    for memo in memos:
        if memo.id == req_memo.id:
            memo.content = req_memo.content
            return "성공"
    return "실패"


@app.delete("/memos/{memo_id}")
def delete_memo(memo_id):
    for idx, memo in enumerate(memos):
        if memo.id == memo_id:
            memos.pop(idx)
            return "성공"
    return "실패"


app.mount("/", StaticFiles(directory="static", html=True), name="static")

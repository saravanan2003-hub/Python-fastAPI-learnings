from fastapi import FastAPI
from pydantic import BaseModel

class New_Article(BaseModel):
    title : str
    description : str
    author : str


    
app = FastAPI(title = "testproject")
@app.get("/")
def hello():
    return {"status" : 200}

@app.get("/v1/articles")
def get_articles():
    return {"data" : []}

@app.get("/v1/articles/{id}")
def get_article_by_id(id : str):
    print(id)
    return {"data" : {"id": id}}

@app.post("/v1/article")
def create_article(new_article:New_Article):
    print(new_article)
    return {"status" : 201}

@app.put("/v1/article/{id}")
def updated_article(updated_article : New_Article):
    print(updated_article)
    return {"status" : 201}

@app.delete("/v1/article/{id}")
def delete_article():
    return {"status" : 200}

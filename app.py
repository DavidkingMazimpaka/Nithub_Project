from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from scrapp_annotate import scrape_news, annotate_sentences

app = FastAPI()

class URLRequest(BaseModel):
    url: str

@app.post("/predict")
async def predict_sentiment(request: URLRequest):
    try:
        sentences = scrape_news(request.url)
        annotated_sentences = annotate_sentences(sentences)
        return annotated_sentences
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
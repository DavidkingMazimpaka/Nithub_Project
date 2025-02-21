import random
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from scrapp_annotate import scrape_news, annotate_sentences
from optimize_model import annotate_sentences_light

app = FastAPI()

class URLRequest(BaseModel):
    url: str

@app.post("/predict")
async def predict_sentiment(request: URLRequest):
    try:
        sentences = scrape_news(request.url)
        model_type = random.choice(['baseline', 'optimized'])

        if model_type == 'baseline':
            annotated_sentences = annotate_sentences(sentences)
        else:
            annotated_sentences = annotate_sentences_light(sentences)
        
        response = {
            'model_type': model_type,
            'results': annotated_sentences
        }
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

pipeline = joblib.load("symptom_model.pkl")
le = joblib.load("label_encoder.pkl")
best_thresholds = joblib.load("best_thresholds.pkl")

app = FastAPI()

class SymptomRequest(BaseModel):
    age: int
    gender: str
    yes_symptoms_texts: str

@app.post("/predict_symptoms")
def predict_symptoms(request: SymptomRequest):
    input_df = pd.DataFrame([{
        "age": request.age,
        "gender": request.gender,
        "yes_symptoms_texts": request.yes_symptoms_texts.lower().strip()
    }])
    
    prob = pipeline.predict_proba(input_df)[0]
    classes = le.classes_
    
    class_probs = list(zip(classes, prob))
    
    class_probs_sorted = sorted(class_probs, key=lambda x: x[1], reverse=True)
    
    top5 = class_probs_sorted[:5]
    
    recommended = [{"symptom": c, "probability": float(p)} for c, p in top5]
    
    return {"recommended_symptoms": recommended}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

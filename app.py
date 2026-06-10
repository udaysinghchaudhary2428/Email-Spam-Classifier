from fastapi import FastAPI, HTTPException
from schema.userinput import DataValidator,PredictionResponse
from schema.text import transform_text
import joblib

app = FastAPI(title="Email Spam Detection API",
              description="API for classifying email/SMS text as spam or ham",
              version="1.0.0")

model = joblib.load("model/spam_classifier.joblib")
le = joblib.load("model/label_encoder.joblib")


@app.get("/")
def read_root():
    return {"message":"Email Spam Detection API is running"}

@app.post(
    "/predict",
    tags=["Prediction"],
    response_model=PredictionResponse
)
def predict(data: DataValidator):

    try:
        processed_text = transform_text(data.text)

        prediction = model.predict([processed_text])[0]

        probabilities = model.predict_proba([processed_text])[0]

        label = le.inverse_transform([prediction])[0]

        confidence = round(float(max(probabilities)), 4)

        return PredictionResponse(
            prediction=label,
            confidence=confidence
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )

       
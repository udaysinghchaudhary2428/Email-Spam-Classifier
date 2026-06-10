from pydantic import BaseModel, Field, field_validator
from typing import Annotated, Literal


class DataValidator(BaseModel):
    text: Annotated[
        str,
        Field(
            min_length=1,
            description="Email/SMS text to classify"
        )
    ]

    @field_validator("text")
    @classmethod
    def validate_text(cls, value):
        if not value.strip():
            raise ValueError("Text cannot be empty")

        return value.strip()


class PredictionResponse(BaseModel):
    prediction: Literal["spam", "ham"]

    confidence: Annotated[
        float,
        Field(
            ge=0.0,
            le=1.0,
            description="Prediction confidence score"
        )
    ]
from fastapi import FastAPI,Query
from openai import OpenAI

from typing import Annotated


app = FastAPI()
openai_client = OpenAI(api_key="openAI_api_key")


@app.get("/health-check")
def health_check_service():
    return {"status": "The service is up and Running"}


@app.get("/api/chat")
def chat_controller(
    model_name : Annotated[str,Query(title = "Gen AI model name")],
    prompt: Annotated[str,Query(title = 'Prompt to the GenAI model')] = "Inspire me"):

    response = openai_client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    statement = response.choices[0].message.content.strip()
    return {"statement": statement}
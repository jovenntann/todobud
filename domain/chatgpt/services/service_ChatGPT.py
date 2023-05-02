import openai
import logging
from typing import List

# Library: django-environ
import environ
import os

import logging
logger = logging.getLogger(__name__)

env = environ.Env()
environ.Env.read_env()

openai.api_key = os.environ.get('OPENAI_API_KEY')
model_engine = "gpt-3.5-turbo"


def ask_assistant(question: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question},
        ]
    )
    logging.info(response)
    answer = response.choices[0].text.strip()
    logging.info(answer)
    return answer


def get_answer_to_question(question: str) -> str:
    answer = ask_assistant(question)
    return answer



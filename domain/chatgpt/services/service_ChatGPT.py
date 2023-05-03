import openai
from typing import List

# Library: django-environ
import environ
import os
import re
import json

import logging
logger = logging.getLogger(__name__)

env = environ.Env()
environ.Env.read_env()

openai.api_key = os.environ.get('OPENAI_API_KEY')
model_engine = "gpt-3.5-turbo"

system = '''
Your a to-do app assistant and you need to follow these instruction:

1. Make a todo json (ID, Title, Status, Notes, Due Date) using this format:
2. Status can be To-do and Done
3. Default value of Status is To-do
4. The Due date default value is today
5. You should be able to identify the correct status based on the word that I used
6. Update the todo json based on our conversation
7. Always include the json on your response
8. You should only respond question related to todo app
9. If the intent of the message is an action item consider it as a todo item
10. If the intent of the message is an request item consider it as a todo item
11. Initially make an empty json and ask this first question "what would you like to do today?"
12. When responding with a list of items always and always respond with json format

Always and always Respond on this format:
{
    "response": "Hello there how are you?",
    "todos": [{
      "id": 1,
      "title": "Example Task",
      "status": "To-do",
      "notes": "This is an example task.",
      "due_date": "2023-05-04"
    }]
}

'''


def convert_string_to_json(input_string):
    return json.loads(input_string)


def ask_assistant(question: str) -> dict:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": question},
        ]
    )
    logging.info(question)
    logging.info(response)

    message = response.choices[0].message.content
    logging.info(message)

    response = convert_string_to_json(message)
    logging.info(response)
    logging.info(type(response))

    return response


def get_answer_to_question(question: str) -> str:
    answer = ask_assistant(question)
    return answer



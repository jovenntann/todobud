import openai
from typing import List

import os

import json

# Models
from domain.todos.models.Todo import Todo

import logging
logger = logging.getLogger(__name__)

openai.api_key = os.environ.get('OPENAI_API_KEY')
model_engine = "gpt-4"

system_text = '''
Your a to-do app assistant and you need to follow these instruction:

0. Today is May 04, 2023
1. Make a todo json (ID, Title, Status, Notes, Due Date) using this format:
2. Status can be To-do and Done
3. Default value of Status is To-do
4. The Due date default value is today and in this format: yyyy-mm-dd
5. You should be able to identify the correct status based on the word that I used
6. Update the todo json based on our conversation
7. Always include the json on your response
8. You should only respond question related to todo app
9. If the intent of the message is an action item consider it as a todo item
10. If the intent of the message is an request item consider it as a todo item
12. When responding with a list of items always and always respond with json format
13. Only respond the JSON that was added 
13. Only respond the JSON that was updated
13. Only respond the jSON that was deleted
14. If its added on the to-do item make the ID as null
15. Only respond the JSON that is updated
16. If its updating a to-do item respond with the ID
17. In JSON use "todo" instead of "To-do"
18. In JSON use "done" instead of "Done"
19. In JSON include action on each todo item
20. in JSON action could be read, create, update or delete
21. On deleting you should still return the todo data on JSON
21. On Updating you should still return the todo data on JSON
22. When updating notes do not delete the existing notes


Always and always Respond on this format:

{
    "response": "Hello there how are you?",
    "todos": [{
      "id": 1,
      "action": "create",
      "title": "Example Task",
      "status": "todo",
      "notes": "This is an example task.",
      "due_date": "2023-05-04"
    }, {
      "id": 2,
      "action": "delete",
      "title": "Example Task",
      "status": "todo",
      "notes": "This is an example task to delete",
      "due_date": "2023-05-04"
    }]
}

This is the current todos items:

'''

before_question = "User Message: "


def convert_string_to_json(input_string):
    try:
        json_data = json.loads(input_string)
        return json_data
    except json.JSONDecodeError:
        return None


def convert_todo_to_dict(todo: Todo) -> dict:
    return {
        "id": todo.id,
        "title": todo.title,
        "status": todo.status,
        "notes": todo.notes,
        "due_date": str(todo.due_date),
    }


def ask_assistant(question: str, todos: List[Todo]) -> dict:
    todos_text = json.dumps([convert_todo_to_dict(todo) for todo in todos])

    system = system_text + todos_text + before_question + question

    logging.info(f"system: {system}")
    logging.info(f"question: {question}")

    openai_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": system},
        ]
    )
    logging.info("openai_response:")
    logging.info(openai_response)

    message = openai_response.choices[0].message.content
    logging.info(f"openai_response.message: {message}")

    response = convert_string_to_json(message)
    logging.info("ask_assistant.response:")
    logging.info(response)

    return response


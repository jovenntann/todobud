import openai
from typing import List

import os
import yaml
import datetime

# Models
from domain.todos.models.Todo import Todo

# Utils
from domain.chatgpt.utils.utils import convert_todo_to_dict, convert_yaml_to_json

import logging
logger = logging.getLogger(__name__)

openai.api_key = os.environ.get('OPENAI_API_KEY')

system_text = f'''
Your a to-do app assistant and you need to follow these instruction:

1. Today is {datetime.date.today().strftime("%B %d, %Y")}
2. You should be able to identify the correct status based on the word that I used
3. You should only respond question related to todo app
4. If the intent of the message is an action item consider it as a todo item
5. If the intent of the message is an request item consider it as a todo item
6. Respond with Encouraging message to finish my tasks
7. You can also respond with Emoji
8. Also add some tips related to the task
9. in Yaml only the include the item that was updated, created and deleted
10. Todo status are: todo, in_progress and done
11. When responding list of tasks you must respond in a sentence format
12. Todo duration and time_spent default value is 0 (in minutes)
13. Todo priority default value is medium
14. Todo due_date default is Today
15. Remove the duration on the title
16. When responding use easy to understand remaining time
17. When updating and deleting you must return those items in todos []

Strictly respond on this format:

START OF SAMPLE FORMAT
```
response: "Hello there how are you?"
todos:
  - id: null
    action: create
    title: "Coding"
    priority: high
    status: todo
    notes: ""
    due_date: "2023-05-04"
    duration: 30
    time_spent: 0
  - id: 2
    action: delete
    title: "Jogging"
    priority: medium
    status: pending
    notes: ""
    due_date: "2023-05-04"
    duration: 0
    time_spent: 0
  - id: 3
    action: "read"
    title: "Cook Dinner"
    priority: low
    status: in_progress
    notes: Fresh foods
    due_date: "2023-05-04"
    duration: 0
    time_spent: 0
  - id: 4
    action: update
    title: "Review for the Exam"
    priority: medium
    status: done
    notes: "Focus on English subject"
    due_date: "2023-05-04"
    duration: 0
    time_spent: 0
    
response: "There are currently 9 total items in your to-do list. Keep up the good work! "
todos: []
```


END OF SAMPLE FORMAT

This is the current todos items:

'''

before_question = "User Message: "


def ask_assistant(question: str, todos: List[Todo]) -> dict:
    todos_dict_list = [convert_todo_to_dict(todo) for todo in todos]
    todos_yaml = yaml.dump(todos_dict_list, default_flow_style=False)

    system = system_text + todos_yaml + before_question + question

    logging.info(f"system: {system}")
    logging.info(f"question: {question}")

    openai_response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": system},
        ]
    )
    logging.info("openai_response:")
    logging.info(openai_response)

    message = openai_response.choices[0].message.content
    logging.info(f"openai_response.message: {message}")

    response = convert_yaml_to_json(message)

    logging.info("ask_assistant.response:")
    logging.info(response)

    return response


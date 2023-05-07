import json
import yaml

# Models
from domain.todos.models.Todo import Todo

import logging
logger = logging.getLogger(__name__)


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
        "priority": todo.priority,
        "status": todo.status,
        "notes": todo.notes,
        "due_date": str(todo.due_date),
        "duration": todo.duration,
        "time_spent": todo.time_spent
    }


def convert_json_to_yaml(json_data):
    try:
        # Load the JSON data as a Python dictionary
        data = json.loads(json_data)
        # Dump the dictionary as YAML string
        yaml_data = yaml.dump(data, default_flow_style=False)
        return yaml_data
    except json.JSONDecodeError:
        return None


def convert_yaml_to_json(yaml_data: str) -> dict:
    try:
        # Load the YAML data as a Python dictionary
        data = yaml.safe_load(yaml_data)
        # Convert the dictionary to a JSON object
        json_data = json.loads(json.dumps(data))
        return json_data
    except yaml.YAMLError:
        logging.info("Invalid YAML format")
        return {}

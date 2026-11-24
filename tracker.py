from datetime import datetime
import json
from typing import List, Dict



def add_habit(habits: dict, habit_name: str) -> None:
    if habit_name in habits:
        raise ValueError(f"Habit '{habit_name}' already exists.")
    habits[habit_name] = {
        "created_at": datetime.now().isoformat(),
        "completed_dates": []
    }


def get_all_habits_names(habits: dict) -> List[str]:
    return list(habits.keys())


def save_habits(habits: dict, path: str) -> None:
    try:
        with open(path, 'w') as f:
            json.dump(habits, f, indent=2)      
    except IOError as e:
        print(f"Error saving habits to {path}: {e}")


def load_habits(path: str) -> Dict[str, dict]:
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as e:
        print(f"Error loading habits from {path}: {e}")
        return {}
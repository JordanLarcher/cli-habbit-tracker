from datetime import datetime


def add_habit(habits: dict, habit_name: str) -> None:
    """Add a new habit to the habits dictionary."""
    if habit_name in habits:
       raise ValueError(f"Habit '{habit_name}' already exists.") 
    else:
        habits[habit_name] = [datetime.today().isoformat()]
        print(f"Habit '{habit_name}' added.")


def list_habits(habits: dict) -> list[str]:
    """List all habits."""
    return list(habits.keys())
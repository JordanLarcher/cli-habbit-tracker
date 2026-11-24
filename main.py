import argparse
from tracker import add_habit, get_all_habits_names, save_habits, load_habits
def main():
    habits = load_habits('habits.json')
    parser = argparse.ArgumentParser(description="Habit Tracker CLI")
    subparsers = parser.add_subparsers(dest='command', required=True)   
    add_parser = subparsers.add_parser('add', help='Add a new habit')
    add_parser.add_argument('name', type=str, help='Name of the habit to add')
    list_parser = subparsers.add_parser('list', help='List all habits')
    list_parser.add_argument('--all', action='store_true', help='List all habits')  
    args = parser.parse_args()

    if args.command == 'add':
        habit_name = args.name
        try:
            add_habit(habits, habit_name)
            save_habits(habits, 'habits.json')
        except ValueError as e:
            print(e)
    elif args.command == 'list':
        habits_list = get_all_habits_names(habits)
        if habits_list:
            print("Habits:")
            for habit in habits_list:
                print(f"- {habit}")
        else:
            print("No habits found.")

if __name__ == "__main__":
    main()
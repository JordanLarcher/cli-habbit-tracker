import argparse
from tracker import add_habit, list_habits
def main():
    habits = {}
    parser = argparse.ArgumentParser(description="Habit Tracker CLI")
    subparsers = parser.add_subparsers(dest='command', required=True)   
    add_parser= subparsers.add_parser('add', help='Add a new habit')
    add_parser.add_argument('name')
    args = parser.parse_args()

    if args.command == 'add':
        habit_name = args.habit
        try:
            add_habit(habits, habit_name)
        except ValueError as e:
            print(e)
    elif args.command == 'list':
        habits_list = list_habits(habits)
        if habits_list:
            print("Habits:")
            for habit in habits_list:
                print(f"- {habit}")
        else:
            print("No habits found.")

if __name__ == "__main__":
    main()
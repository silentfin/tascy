import sqlite3
import argparse


class TascyDB:
    def __init__(self):
        self.con = sqlite3.connect("tascy.db")
        self.cursor = self.con.cursor()
        self.cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS tascy (
        id INTEGER PRIMARY KEY,
        task TEXT NOT NULL,
        is_done INTEGER DEFAULT 0)
    """
        )

    def insert_task(self, task):
        self.cursor.execute("INSERT INTO tascy (task) VALUES (?)", (task,))
        self.con.commit()

    def delete_task(self, id):
        self.cursor.execute("DELETE FROM tascy WHERE id = ?", (id,))
        self.con.commit()

    def update_task(self, id, updated_task):
        self.cursor.execute(
            "UPDATE tascy SET task = ? WHERE id = ?", (updated_task, id)
        )
        self.con.commit()

    def mark_done(self, id):
        self.cursor.execute("UPDATE tascy SET is_done = ? WHERE id = ?", (1, id))
        self.con.commit()

    def mark_undone(self, id):
        self.cursor.execute("UPDATE tascy SET is_done = ? WHERE id = ?", (0, id))
        self.con.commit()

    def mark_done_all(self):
        self.cursor.execute("UPDATE tascy SET is_done = ?", (1,))
        self.con.commit()

    def mark_undone_all(self):
        self.cursor.execute("UPDATE tascy SET is_done = ?", (0,))
        self.con.commit()

    def search_task(self, keyword):
        self.cursor.execute("SELECT * FROM tascy WHERE task LIKE ?", (f"%{keyword}%",))
        tasks = self.cursor.fetchall()
        for task in tasks:
            print(f"ID: {task[0]}, Task: {task[1]}, Done: {'Yes' if task[2] else 'No'}")

    def count_tasks(self):
        self.cursor.execute("SELECT COUNT(*) FROM tascy")
        task = self.cursor.fetchone()[0]
        print(f"Total Tasks: {task}")

    def get_task(self, id):
        self.cursor.execute("SELECT * FROM tascy WHERE id = ?", (id,))
        task = self.cursor.fetchone()
        print(f"ID: {task[0]}, Task: {task[1]}, Done: {'Yes' if task[2] else 'No'}")

    def show_tasks(self):
        self.cursor.execute("SELECT * FROM tascy")
        tasks = self.cursor.fetchall()
        for task in tasks:
            print(f"ID: {task[0]}, Task: {task[1]}, Done: {'Yes' if task[2] else 'No'}")

    def show_pending_tasks(self):
        self.cursor.execute("SELECT * FROM tascy WHERE is_done = 0")
        tasks = self.cursor.fetchall()
        for task in tasks:
            print(f"ID: {task[0]}, Task: {task[1]}, Done: {'Yes' if task[2] else 'No'}")

    def show_finished_tasks(self):
        self.cursor.execute("SELECT * FROM tascy WHERE is_done = 1")
        tasks = self.cursor.fetchall()
        for task in tasks:
            print(f"ID: {task[0]}, Task: {task[1]}, Done: {'Yes' if task[2] else 'No'}")

    def delete_all(self):
        self.cursor.execute("DELETE FROM tascy")
        self.con.commit()

    def close(self):
        self.con.close()


def parse_args():
    parser = argparse.ArgumentParser(description="Tascy - CLI To-Do List")
    parser.add_argument("-a", "--add", help="Add a new task")
    parser.add_argument("-d", "--delete", type=int, help="Delete a task by ID")
    parser.add_argument(
        "-u", "--update", nargs=2, metavar=("ID", "TASK"), help="Update task text by ID"
    )
    parser.add_argument("-f", "--done", type=int, help="Mark task as done by ID")
    parser.add_argument("-r", "--undone", type=int, help="Mark task as undone by ID")
    parser.add_argument(
        "--done-all", action="store_true", help="Mark all tasks as done"
    )
    parser.add_argument(
        "--undone-all", action="store_true", help="Mark all tasks as undone"
    )
    parser.add_argument("-s", "--show", action="store_true", help="Show all tasks")
    parser.add_argument(
        "--show-pending", action="store_true", help="Show pending tasks"
    )
    parser.add_argument(
        "--show-finished", action="store_true", help="Show finished tasks"
    )
    parser.add_argument("--search", help="Search tasks by keyword")
    parser.add_argument("--count", action="store_true", help="Count total tasks")
    parser.add_argument("--get", type=int, help="Get task by ID")
    parser.add_argument(
        "--delete-all", action="store_true", help="Delete all tasks (clear table)"
    )
    return parser.parse_args()


def main(tascy):
    while True:
        operation = input("Enter your choice: ").lower()

        if operation == "q":
            print("Goodbye!")
            break
        elif operation == "a":
            task = input("Enter new task: ")
            tascy.insert_task(task)
            print("Task added.")
        elif operation == "d":
            try:
                id = int(input("Enter task ID to delete: "))
                tascy.delete_task(id)
                print(f"Task {id} deleted.")
            except ValueError:
                print("Invalid ID. Please enter a number.")
        elif operation == "u":
            try:
                id = int(input("Enter task ID to update: "))
                new_task = input("Enter updated task: ")
                tascy.update_task(id, new_task)
                print(f"Task {id} updated.")
            except ValueError:
                print("Invalid ID. Please enter a number.")
        elif operation == "f":
            try:
                id = int(input("Enter task ID to mark as finished: "))
                tascy.mark_done(id)
                print(f"Task {id} marked as finished.")
            except ValueError:
                print("Invalid ID. Please enter a number.")
        elif operation == "r":
            try:
                id = int(input("Enter task ID to mark as undone: "))
                tascy.mark_undone(id)
                print(f"Task {id} marked as undone.")
            except ValueError:
                print("Invalid ID. Please enter a number.")
        elif operation == "fa":
            tascy.mark_done_all()
            print("All tasks marked as done.")
        elif operation == "ra":
            tascy.mark_undone_all()
            print("All tasks marked as undone.")
        elif operation == "s":
            tascy.show_tasks()
        elif operation == "sp":
            tascy.show_pending_tasks()
        elif operation == "sf":
            tascy.show_finished_tasks()
        elif operation == "se":
            keyword = input("Enter search keyword: ")
            tascy.search_task(keyword)
        elif operation == "c":
            tascy.count_tasks()
        elif operation == "g":
            try:
                id = int(input("Enter task ID to get: "))
                tascy.get_task(id)
            except ValueError:
                print("Invalid ID. Please enter a number.")
        elif operation == "delall":
            confirm = input("Are you sure? This will delete ALL tasks! (y/n): ")
            if confirm.lower() == "y":
                tascy.delete_all()
                print("All tasks deleted.")
            else:
                print("Deletion aborted.")
        elif operation == "h":
            print(
                """\nAll operations:
h  - Help
q  - Quit
a  - Add task
d  - Delete task
u  - Update task
f  - Mark task as finished
r  - Mark task as undone
fa - Mark all tasks done
ra - Mark all tasks undone
s  - Show all tasks
sp - Show pending tasks
sf - Show finished tasks
se - Search tasks
c  - Count total tasks
g  - Get task by ID
delall - Delete all tasks\n"""
            )
        else:
            print("Invalid input, please try again. Or type 'h' for help")


if __name__ == "__main__":
    tascy = TascyDB()
    try:
        args = parse_args()
        if args.add:
            tascy.insert_task(args.add)
        elif args.delete:
            tascy.delete_task(args.delete)
        elif args.update:
            id, new_task = args.update
            tascy.update_task(int(id), new_task)
        elif args.done:
            tascy.mark_done(args.done)
        elif args.undone:
            tascy.mark_undone(args.undone)
        elif args.done_all:
            tascy.mark_done_all()
        elif args.undone_all:
            tascy.mark_undone_all()
        elif args.show:
            tascy.show_tasks()
        elif args.show_pending:
            tascy.show_pending_tasks()
        elif args.show_finished:
            tascy.show_finished_tasks()
        elif args.search:
            tascy.search_task(args.search)
        elif args.count:
            tascy.count_tasks()
        elif args.get:
            tascy.get_task(args.get)
        elif args.delete_all:
            tascy.delete_all()
        else:
            main(tascy)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        tascy.close()


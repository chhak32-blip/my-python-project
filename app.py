from task_manager import TaskManager

def main():
    tm = TaskManager()
    print("\n📋 Your Task List:")
    tm.list_tasks()

    print("\n➕ Adding new tasks...")
    tm.add_task("Write Jenkins pipeline")
    tm.add_task("Review PRs")
    tm.list_tasks()

    print("\n✅ Completing task 0...")
    tm.complete_task(0)
    tm.list_tasks()

if __name__ == "__main__":
    main()

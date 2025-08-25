from task_manager import TaskManager
import os

def test_add_and_complete_task():
    if os.path.exists("tasks.json"):
        os.remove("tasks.json")

    tm = TaskManager()
    tm.add_task("Test Task")
    assert tm.tasks[-1]['description'] == "Test Task"
    assert not tm.tasks[-1]['completed']

    tm.complete_task(0)
    assert tm.tasks[0]['completed']

if __name__ == "__main__":
    print("✅ Running tests...")
    test_add_and_complete_task()
    print("✅ All tests passed.")

from task_manager import TaskManager
import os

# Use a separate file for testing
TEST_TASKS_FILE = "test_tasks.json"

def test_add_and_complete_task():
    if os.path.exists(TEST_TASKS_FILE):
        os.remove(TEST_TASKS_FILE)

    tm = TaskManager()
    tm.tasks = []  # clear
    tm.save_tasks = lambda: open(TEST_TASKS_FILE, 'w').write('[]')  # override save

    tm.add_task("Test Task")
    assert tm.tasks[-1]['description'] == "Test Task"
    assert not tm.tasks[-1]['completed']

    tm.complete_task(0)
    assert tm.tasks[0]['completed']

if __name__ == "__main__":
    print("✅ Running tests...")
    test_add_and_complete_task()
    print("✅ All tests passed.")

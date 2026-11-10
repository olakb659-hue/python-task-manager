from src.main import add_task, tasks

def test_add_task():
    add_task("test")
    assert len(tasks) == 1
    
tasks = []

def add_task(title):
    tasks.append({"title": title, "done": False})

def list_tasks():
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t['title']}")

def remove_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)

def main():
    add_task("Выучить Git")
    add_task("Сдать лабораторную")
    list_tasks()

if __name__ == "__main__":
    main()
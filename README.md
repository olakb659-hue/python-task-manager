# python-task-manager
Консольный менеджер задач на Python: добавление, просмотр и удаление задач
## Требования
- Python 3.8 или новее
- pytest (для запуска тестов)
## Установка
```bash
git clone https://github.com/olakb659-hue/python-task-manager.git
cd python-task-manager
pip install -r requirements.txt
```
## Запуск
```bash
python src/main.py
```
## Запуск тестов
```bash
pytest
```
## Функции
| Функция | Описание |
|---------|----------|
| `add_task(title)` | Добавляет новую задачу в список |
| `list_tasks()` | Выводит все задачи с номерами |
| `remove_task(index)` | Удаляет задачу по индексу |
| `main()` | Точка входа в программу |

## Структура проекта
```
python-task-manager/
├── src/
│   └── main.py
├── tests/
│   └── test_main.py
├── README.md
├── requirements.txt
└── .gitignore
```
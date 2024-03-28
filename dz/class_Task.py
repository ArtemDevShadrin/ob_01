class Task:
    task_list = []  # Список задач, объявленный внутри класса

    def __init__(self, description, deadline):
        self.description = description  # описание задачи
        self.deadline = deadline  # срок выполнения
        self.status = False  # статус выполнения задачи (по умолчанию False - не выполнено)
        Task.task_list.append(self)  # Добавляем созданную задачу в список задач класса

    def mark_as_completed(self):
        self.status = True  # отмечаем задачу как выполненную

    @classmethod
    def display_current_tasks(cls):
        print("Текущие задачи (не выполненные):")
        for index, task in enumerate(cls.task_list, start=1):
            if not task.status:
                print(f"{index}. {task}")

    def __str__(self):
        status = "Выполнено" if self.status else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {status}"

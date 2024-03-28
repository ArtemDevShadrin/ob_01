from dz.class_Task import Task

task1 = Task("Подготовить отчет", "10.03.2024")
task2 = Task("Провести собрание", "15.03.2024")

task1.mark_as_completed()

Task.display_current_tasks()

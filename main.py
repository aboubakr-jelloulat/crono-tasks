import json
import os
from Task import Task
import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer()
console = Console()
TASK_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as f:
        data = json.load(f)
        return [Task.deserialize(item) for item in data]

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump([task.serialize() for task in tasks], f, indent=4)

tasks = load_tasks()

@app.command()
def add(title: str, start: str, end: str):
    task = Task(title, start, end)
    tasks.append(task)
    save_tasks(tasks)
    console.print(f"Task added: {title}", style="bold green")

@app.command()
def list_tasks():
    if not tasks:
        console.print("No tasks yet.", style="bold yellow")
        return
    
    table = Table(title="Tasks")
    table.add_column("ID", style="cyan", justify="center")
    table.add_column("Title", style="magenta")
    table.add_column("Start")
    table.add_column("End")
    table.add_column("Duration (min)")
    table.add_column("Status", style="bold")

    for i, task in enumerate(tasks, 1):
        table.add_row(
            str(i),
            task.title,
            task.start_time.strftime("%H:%M"),
            task.end_time.strftime("%H:%M"),
            f"{task.duration:.1f}",
            task.status()
        )

    console.print(table)

@app.command()
def complete(task_id: int):
    if 0 < task_id <= len(tasks):
        tasks[task_id - 1].complete()
        save_tasks(tasks)
        console.print(f"Task {task_id} marked as completed!", style="bold green")
    else:
        console.print("Invalid task ID", style="bold red")

@app.command()
def delete(task_id: int):
    if 0 < task_id <= len(tasks):
        task = tasks.pop(task_id - 1)
        save_tasks(tasks)
        console.print(f"Task deleted: {task.title}", style="bold red")
    else:
        console.print("Invalid task ID", style="bold red")

if __name__ == "__main__":
    app()
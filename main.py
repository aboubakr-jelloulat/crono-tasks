from Task import Task  
import typer
from rich.console import Console

app = typer.Typer()
console = Console()

tasks = []

@app.command()
def add(title: str, start: str, end: str):
    task = Task(title, start, end)
    tasks.append(task)
    console.print(f"Task added: {title}", style="bold green")

@app.command()
def list_tasks():
    if not tasks:
        console.print("No tasks yet.", style="bold yellow")
        return 
    for i, task in enumerate(tasks, 1):
        console.print(f"[{i}] {task.title} | Duration: {task.duration:.1f} mins | Status: {task.status()}")

@app.command()
def complete(task_id: int):
    if 0 < task_id <= len(tasks):
        tasks[task_id - 1].complete()
        console.print(f"Task {task_id} marked as completed!", style="bold green")
    else:
        console.print("Invalid task ID", style="bold red")

if __name__ == "__main__":
    app()
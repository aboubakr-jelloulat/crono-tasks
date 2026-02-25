from datetime import datetime

class Task:
    def __init__(self, title: str, start_time: str, end_time: str):
        self.title = title
        self.start_time = datetime.strptime(start_time, "%H:%M")
        self.end_time = datetime.strptime(end_time, "%H:%M")
        self.completed = False

    @property
    def duration(self):
        diff = self.end_time - self.start_time
        return diff.total_seconds() / 60

    def complete(self):
        self.completed = True

    def status(self) -> str:
        now = datetime.now()
        if self.completed:
            return "Finished"
        elif self.start_time <= now <= self.end_time:
            return "In Progress"
        elif now < self.start_time:
            return "Not Yet"
        else:
            return "Overdue"

    def serialize(self) -> dict:
        return
        {
            "title": self.title,
            "start time": self.start_time.strftime("%H:%M"),
            "end time": self.end_time.strftime("%H:%M"),
            "completed": self.completed
        }
    
    @staticmethod
    def deserialize(data: dict):
        return Task(
            title = data["title"],
            start_time = data["start time"],
            end_time = data["end time"],
            completed = data.get("completed", False)
        )

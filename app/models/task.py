from dataclasses import dataclass, asdict  # saves us from writing (__init__, __repr__)
from datetime import datetime #let's us report when a task was created
import uuid #generates unique IDs (for later deleting/editing tasks)

@dataclass #this class mainly stores data
class Task:
    id: int
    title: str
    created_at: str
    completed: bool = False

    @staticmethod
    def create(title: str, id: int) -> "Task":
        return Task(
            id=id,
            title=title,
            created_at=datetime.utcnow().isoformat(),
            completed=False
        )

    def to_dict(self):
        return asdict(self)
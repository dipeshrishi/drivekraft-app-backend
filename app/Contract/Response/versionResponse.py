
from datetime import datetime

class versionResponse:
    def __init__(self, id, key, value, created_at, updated_at):
        self.id = id
        self.key = key
        self.value = value
        self.created_at = datetime.fromisoformat(created_at) if created_at else None
        self.updated_at = datetime.fromisoformat(updated_at) if updated_at else None

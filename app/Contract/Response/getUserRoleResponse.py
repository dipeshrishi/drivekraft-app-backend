class Role:
    def __init__(self, created_at, id, label, name, pivot, updated_at):
        self.created_at = created_at
        self.id = id
        self.label = label
        self.name = name
        self.pivot = Pivot(**pivot) if pivot else None
        self.updated_at = updated_at

class Pivot:
    def __init__(self, role_id, user_id):
        self.role_id = role_id
        self.user_id = user_id




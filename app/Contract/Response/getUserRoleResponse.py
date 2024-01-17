class Role:
    def __init__(self, created_at, id, label, name, pivot, updated_at):
        self.created_at = created_at
        self.id = id
        self.label = label
        self.name = name
        self.pivot = pivot.to_dict() if pivot else None
        self.updated_at = updated_at

    def to_dict(self):
        return {
            'created_at': self.created_at,
            'id': self.id,
            'label': self.label,
            'name': self.name,
            'pivot': self.pivot,
            'updated_at': self.updated_at
        }

class Pivot:
    def __init__(self, role_id, user_id):
        self.role_id = role_id
        self.user_id = user_id

    def to_dict(self):
        return {'role_id': self.role_id, 'user_id': self.user_id}




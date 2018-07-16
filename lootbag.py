class Lootbag:
    def get_all_child_toys(self, child):
        return ['doll']

class Child:
    def set_delivered(self, delivered = False):
        self.delivered = delivered
        return delivered
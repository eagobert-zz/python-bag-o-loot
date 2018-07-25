class Lootbag:
    def __init__(self, delivered = False):
        self.loot = {}
        self.delivered = delivered

    def assign_child_to_bag_and_toy(self, child, toy):
        self.loot[child] = toy

    def remove_child_from_bag(self, child):
        del(self.loot[child])

    def get_all_child_toys(self, child):
        return ['doll']

    def set_delivered_property(self, bool):
        self.delivered = bool

    def list_all_children_assigned_toy(self):
        assigned_children = list()
        for child in self.loot:
            assigned_children.append(child)

        return assigned_children
        




    
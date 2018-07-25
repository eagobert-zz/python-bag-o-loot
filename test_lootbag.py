# Step 1:  Import "unittest"
import unittest
from lootbag import Lootbag


# Step 2:  Create a class to hold the tests
class TestBagOLoot(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.bag = Lootbag()

# Step 3: Create individual tests

    # 3a: Items can be added to bag, and assigned to a child.
    def test_can_add_loot_and_assign_child_to_bag(self):
        expected_result = 'Bear'
        self.bag.assign_child_to_bag_and_toy('Tonya','Bear')
        self.assertIn(expected_result, self.bag.loot['Tonya'])

    # 3b: Items can be removed from bag, per child. Removing ball from the bag should not be allowed. A child's name must be specified.
    def test_can_remove_child_from_bag(self):
        self.bag.remove_child_from_bag('Tonya')
        self.assertNotIn('Tonya', self.bag.loot)

    # 3c: Must be able to list all children who are getting a toy
    def test_can_list_all_children_assigned_toy(self):
        my_bag = Lootbag()
        my_bag.assign_child_to_bag_and_toy("Gerry", "Toy Soldier")
        my_bag.assign_child_to_bag_and_toy('Sandy', 'Rubber Ducky')
        my_bag.assign_child_to_bag_and_toy('Lola', 'Barbie')
        expected_result = ['Gerry', 'Sandy', 'Lola']
        actual_result = my_bag.list_all_children_assigned_toy()
        self.assertListEqual(expected_result, actual_result)

    # 3d: Must be able to list all toys for a given child's name.
    def test_can_get_all_toys_for_a_child(self):
       expected_result = ['doll']
       actual_result = self.bag.get_all_child_toys('Kira')
       self.assertListEqual(expected_result, actual_result)

    # 3e: Must be able to set the delivered property of a child's toys --which defaults to false --to true.
    def test_set_delivered_property_of_childs_toy(self):
        expected_result = True
        self.bag.set_delivered_property(True)
        self.assertEqual(expected_result, self.bag.delivered)


# Step 4: Run Tests
if __name__ == '__main__':
    unittest.main()
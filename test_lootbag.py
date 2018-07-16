# Step 1:  Import "unittest"
import unittest
from lootbag import Lootbag
from lootbag import Child


# Step 2:  Create a class to hold the tests
class TestBagOLoot(unittest.TestCase):

# Step 3: Create individual tests

    # 3a: Items can be added to bag, and assigned to a child.
    # def can_add_loot_and_assign_child_to_bag(self):
    #     my_lootbag = Lootbag()
    #     self.assertEqual()


    # 3b: Items can be removed from bag, per child. Removing ball from the bag should not be allowed. A child's name must be specified.

    # 3c: Must be able to list all children who are getting a toy.

    # 3d: Must be able to list all toys for a given child's name.
    def test_can_get_all_toys_for_a_child(self):
       expected_result = ['doll']
       my_lootbag = Lootbag()
       result = my_lootbag.get_all_child_toys('Kira')
       self.assertEqual(expected_result, result)

    # 3e: Must be able to set the delivered property of a child, which defaults to false to true.
    def test_set_delivered_property_of_child(self):
        my_child = Child()
        expected_result = True
        result = my_child.set_delivered(True)
        self.assertEqual(expected_result, result)

# Step 4: Run Tests
if __name__ == '__main__':
    unittest.main()
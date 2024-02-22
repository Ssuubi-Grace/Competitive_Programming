import random

class RandomizedSet(object):

    def __init__(self):
        self.data = {}
        self.nums = []

    def insert(self, val):
        """
        Inserts an item val into the set if not present.
        Returns true if the item was not present, false otherwise.
        """
        if val not in self.data:
            self.data[val] = len(self.nums)
            self.nums.append(val)
            return True
        return False

    def remove(self, val):
        """
        Removes an item val from the set if present.
        Returns true if the item was present, false otherwise.
        """
        if val in self.data:
            last_index = len(self.nums) - 1
            last_val = self.nums[last_index]
            index = self.data[val]
            self.nums[index], self.nums[last_index] = self.nums[last_index], self.nums[index]
            self.data[last_val] = index
            del self.data[val]
            self.nums.pop()
            return True
        return False

    def getRandom(self):
        """
        Returns a random element from the current set of elements.
        """
        return random.choice(self.nums)

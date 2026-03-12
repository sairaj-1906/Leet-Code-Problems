1import random
2class RandomizedSet:
3
4    def __init__(self):
5        # Stores the actual elements to allow O(1) random access
6        self.elements = []
7        # Stores mapping of value -> index in the 'elements' list
8        self.val_to_index = {}
9
10    def insert(self, val: int) -> bool:
11        if val in self.val_to_index:
12            return False
13        # Add to the end of the list
14        self.elements.append(val)
15        # Record its index in the dictionary
16        self.val_to_index[val] = len(self.elements) - 1
17
18        return True
19
20    def remove(self, val: int) -> bool:
21        if val not in self.val_to_index:
22            return False
23        # Get the index of the element we want to remove
24        idx_to_remove = self.val_to_index[val]
25        # Get the value of the last element in the list
26        last_element = self.elements[-1]
27
28        # Swap the element to remobe with the last element
29        self.elements[idx_to_remove] = last_element
30        self.val_to_index[last_element] = idx_to_remove
31
32        # Remove the last element (which is now the one we wanted to delete)
33        self.elements.pop()
34        del self.val_to_index[val]
35
36        return True
37
38    def getRandom(self) -> int:
39        # random.choice picks a random element from a list in 0(1) time
40        return random.choice(self.elements)
41
42# Your RandomizedSet object will be instantiated and called as such:
43# obj = RandomizedSet()
44# param_1 = obj.insert(val)
45# param_2 = obj.remove(val)
46# param_3 = obj.getRandom()
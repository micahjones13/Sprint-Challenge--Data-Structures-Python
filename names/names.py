import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# 1.5 sec
# for name in names_1:
#     if name in names_2:
#         duplicates.append(name)


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree | key and value are same in these.
    def insert(self, value):
        if value < self.value:
            # go left
            # if there is nothing to the left
            if not self.left:
                # insert it. It's a binary search tree.
                self.left = BinarySearchTree(value)
            # if there is something there, keep going until there isn't!
            else:
                self.left.insert(value)
        else:
            # go right
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True

        if target < self.value:
            # go left
            if not self.left:
                # it's not here
                return False
            else:
                return self.left.contains(target)
        else:
            # target > value, go right
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # just keep going right until you can't, then return that value
        if not self.right:
            return self.value
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    # just modifying values, so no need to return the recursion call
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)


# .1 sec
tree = BinarySearchTree('a')
for name_1 in names_1:
    tree.insert(name_1)
for name_2 in names_2:
    if tree.contains(name_2):
        duplicates.append(name_2)
end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")


"""
#just storing orignal 

duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

"""
